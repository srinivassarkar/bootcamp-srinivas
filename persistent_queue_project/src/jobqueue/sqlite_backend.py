# src/jobqueue/sqlite_backend.py
# Purpose: SQLite-based implementation of PersistentQInterface

import logging
import os
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from uuid import uuid4

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DB_PATH = os.getenv("JOBQUEUE_DB_PATH", "data/queue.db")
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=f"{LOG_DIR}/jobqueue.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class PersistentQSQLite:
    """SQLite-based persistent job queue with robust concurrency and failure handling."""

    def __init__(self, db_path: str = DB_PATH):
        """Initialize queue with SQLite database path and unique consumer ID."""
        self.db_path = db_path
        self.consumer_id = str(uuid4())
        self._init_db()

    def _init_db(self) -> None:
        """Initialize SQLite database with jobs table and indexes."""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY CHECK(length(id) <= 2000),
                    status TEXT NOT NULL CHECK(status IN ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED', 'UNPROCESSABLE', 'CANCELED')),
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    retries INTEGER DEFAULT 0,
                    consumer_id TEXT,
                    last_heartbeat TEXT
                )
            """)
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_status ON jobs(status)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_consumer ON jobs(consumer_id)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_last_heartbeat ON jobs(last_heartbeat)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_updated_at ON jobs(updated_at)")
            conn.commit()
        logger.info("Initialized SQLite job queue database")

    def _get_conn(self) -> sqlite3.Connection:
        """Return a SQLite connection with row factory enabled."""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def enqueue(self, job: str) -> None:
        """Enqueue a job, resetting duplicates to PENDING."""
        if len(job) > 2000:
            logger.error(f"Job ID exceeds 2000 chars: {job[:50]}...")
            raise ValueError("Job ID exceeds 2000 characters")
        now = datetime.now().isoformat()
        with self._get_conn() as conn:
            conn.execute("""
                INSERT INTO jobs (id, status, created_at, updated_at)
                VALUES (?, 'PENDING', ?, ?)
                ON CONFLICT(id) DO UPDATE SET status='PENDING', updated_at=excluded.updated_at
            """, (job, now, now))
            conn.commit()
        logger.info(f"Enqueued job: {job}")

    def dequeue(self) -> Optional[str]:
        """Dequeue a job atomically with row-level locking."""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("BEGIN IMMEDIATE")
            self.check_stalled_jobs(cursor)
            cursor.execute("""
                SELECT id FROM jobs 
                WHERE status = 'PENDING' 
                ORDER BY created_at ASC 
                LIMIT 1 FOR UPDATE
            """)
            row = cursor.fetchone()
            if row:
                job_id = row["id"]
                now = datetime.now().isoformat()
                cursor.execute("""
                    UPDATE jobs 
                    SET status = 'PROCESSING', consumer_id = ?, last_heartbeat = ?, updated_at = ?
                    WHERE id = ?
                """, (self.consumer_id, now, now, job_id))
                conn.commit()
                logger.info(f"Dequeued job: {job_id} by {self.consumer_id}")
                return job_id
            conn.commit()
            return None

    def heartbeat(self) -> None:
        """Update heartbeat for PROCESSING jobs if older than 1 minute."""
        now = datetime.now()
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs 
                SET last_heartbeat = ? 
                WHERE consumer_id = ? AND status = 'PROCESSING' 
                AND COALESCE(last_heartbeat, '1970-01-01') < ?
            """, (now.isoformat(), self.consumer_id, (now - timedelta(minutes=1)).isoformat()))
            conn.commit()

    def complete(self, job_id: str) -> None:
        """Mark a job as COMPLETED if owned by this consumer."""
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs 
                SET status = 'COMPLETED', consumer_id = NULL, last_heartbeat = NULL, updated_at = ? 
                WHERE id = ? AND consumer_id = ?
            """, (datetime.now().isoformat(), job_id, self.consumer_id))
            conn.commit()
        logger.info(f"Completed job: {job_id} by {self.consumer_id}")

    def mark_failed(self, job_id: str) -> None:
        """Mark a job as FAILED or UNPROCESSABLE with retry delay."""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE jobs 
                SET retries = retries + 1, updated_at = ? 
                WHERE id = ? AND consumer_id = ? 
                AND (retries < 3 OR updated_at < datetime('now', '-5 minutes'))
            """, (datetime.now().isoformat(), job_id, self.consumer_id))
            cursor.execute("""
                UPDATE jobs 
                SET status = CASE WHEN retries >= 3 THEN 'UNPROCESSABLE' ELSE 'FAILED' END 
                WHERE id = ? AND consumer_id = ?
            """, (job_id, self.consumer_id))
            conn.commit()
        logger.warning(f"Marked job failed: {job_id}, retries updated")

    def get_status(self) -> List[Dict[str, str]]:
        """Retrieve all job statuses."""
        with self._get_conn() as conn:
            return [dict(row) for row in conn.execute("SELECT * FROM jobs")]

    def resubmit(self, job_id: str) -> None:
        """Reset a FAILED job to PENDING, keeping retries."""
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs 
                SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ? 
                WHERE id = ? AND status = 'FAILED'
            """, (datetime.now().isoformat(), job_id))
            conn.commit()
        logger.info(f"Resubmitted job: {job_id}")

    def cancel(self, job_id: str) -> None:
        """Mark a job as CANCELED."""
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs 
                SET status = 'CANCELED', updated_at = ? 
                WHERE id = ? AND status IN ('PENDING', 'FAILED', 'UNPROCESSABLE')
            """, (datetime.now().isoformat(), job_id))
            conn.commit()
        logger.info(f"Canceled job: {job_id}")

    def check_stalled_jobs(self, cursor=None) -> None:
        """Requeue stalled PROCESSING jobs."""
        cursor = cursor or self._get_conn().cursor()
        cursor.execute("""
            UPDATE jobs 
            SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
            WHERE status = 'PROCESSING' AND last_heartbeat < ?
        """, (datetime.now().isoformat(), (datetime.now() - timedelta(minutes=5)).isoformat()))
        if not cursor.connection.in_transaction:
            cursor.connection.commit()
        logger.info("Checked and requeued stalled jobs")