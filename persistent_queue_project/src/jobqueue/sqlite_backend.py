# src/jobqueue/sqlite_backend.py
"""SQLite-based implementation of PersistentQInterface with heartbeat monitoring."""

import logging
import os
import sqlite3
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from uuid import uuid4

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("JOBQUEUE_DB_PATH", "data/queue.db")
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

logging.basicConfig(
    level=logging.INFO,
    filename=f"{LOG_DIR}/jobqueue.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class PersistentQSQLite:
    """SQLite-backed persistent queue with robust crash recovery and retry logic."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.consumer_id = str(uuid4())
        self._init_db()
        self._running = True
        # Start heartbeat checker thread
        self._heartbeat_thread = threading.Thread(target=self._run_heartbeat_check, daemon=True)
        self._heartbeat_thread.start()

    def _init_db(self) -> None:
        """Initialize SQLite DB with jobs table and indexes."""
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
            for idx in ["status", "consumer_id", "last_heartbeat", "updated_at"]:
                cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{idx} ON jobs({idx})")
            conn.commit()
        logger.info("SQLite queue DB initialized")

    def _get_conn(self) -> sqlite3.Connection:
        """Get thread-safe SQLite connection with row factory."""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _run_heartbeat_check(self) -> None:
        """Periodically check for stalled jobs every 60s."""
        while self._running:
            try:
                with self._get_conn() as conn:
                    self.check_stalled_jobs(conn.cursor())
                    conn.commit()
                threading.Event().wait(60)  # Check every minute
            except Exception as e:
                logger.error(f"Heartbeat check failed: {e}")

    def enqueue(self, job_id: str) -> None:
        """Enqueue a job; resets duplicates to PENDING."""
        if len(job_id) > 2000:
            logger.error(f"Job ID too long: {job_id[:50]}...")
            raise ValueError("Job ID exceeds 2000 characters")
        now = datetime.now().isoformat()
        with self._get_conn() as conn:
            conn.execute("""
                INSERT INTO jobs (id, status, created_at, updated_at)
                VALUES (?, 'PENDING', ?, ?)
                ON CONFLICT(id) DO UPDATE SET status='PENDING', updated_at=excluded.updated_at
            """, (job_id, now, now))
            conn.commit()
        logger.info(f"Enqueued job_id: {job_id}")

    def dequeue(self) -> Optional[str]:
        """Dequeue a job atomically with locking; checks stalled jobs first."""
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
                logger.info(f"Dequeued job_id: {job_id} by {self.consumer_id}")
                return job_id
            conn.commit()
            return None

    def heartbeat(self) -> None:
        """Update heartbeat for PROCESSING jobs owned by this consumer."""
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
        """Mark job as COMPLETED if owned by this consumer."""
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs
                SET status = 'COMPLETED', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
                WHERE id = ? AND consumer_id = ?
            """, (datetime.now().isoformat(), job_id, self.consumer_id))
            conn.commit()
        logger.info(f"Completed job_id: {job_id} by {self.consumer_id}")

    def mark_failed(self, job_id: str) -> None:
        """Mark job as FAILED (retryable) or UNPROCESSABLE (after 3 retries)."""
        now = datetime.now().isoformat()
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE jobs
                SET retries = retries + 1, updated_at = ?
                WHERE id = ? AND consumer_id = ?
                AND (retries < 3 OR updated_at < datetime('now', '-5 minutes'))
            """, (now, job_id, self.consumer_id))
            cursor.execute("""
                UPDATE jobs
                SET status = CASE WHEN retries >= 3 THEN 'UNPROCESSABLE' ELSE 'FAILED' END
                WHERE id = ? AND consumer_id = ?
            """, (job_id, self.consumer_id))
            conn.commit()
        logger.warning(f"Marked job_id failed: {job_id}, retries updated")

    def get_status(self) -> List[Dict[str, str]]:
        """Retrieve all job statuses."""
        with self._get_conn() as conn:
            return [dict(row) for row in conn.execute("SELECT * FROM jobs")]

    def resubmit(self, job_id: str) -> None:
        """Reset FAILED job to PENDING for retry."""
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs
                SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ? 
                WHERE id = ? AND status = 'FAILED'
            """, (datetime.now().isoformat(), job_id))
            conn.commit()
        logger.info(f"Resubmitted job_id: {job_id}")

    def cancel(self, job_id: str) -> None:
        """Mark job as CANCELED if allowed."""
        with self._get_conn() as conn:
            conn.execute("""
                UPDATE jobs
                SET status = 'CANCELED', updated_at = ?
                WHERE id = ? AND status IN ('PENDING', 'FAILED', 'UNPROCESSABLE')
            """, (datetime.now().isoformat(), job_id))
            conn.commit()
        logger.info(f"Canceled job_id: {job_id}")

    def check_stalled_jobs(self, cursor: Optional[sqlite3.Cursor] = None) -> None:
        """Requeue stalled PROCESSING jobs (no heartbeat > 5 mins)."""
        cursor = cursor or self._get_conn().cursor()
        cursor.execute("""
            UPDATE jobs
            SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
            WHERE status = 'PROCESSING' AND last_heartbeat < ?
        """, (datetime.now().isoformat(), (datetime.now() - timedelta(minutes=5)).isoformat()))
        if not cursor.connection.in_transaction:
            cursor.connection.commit()
        logger.info("Checked and requeued stalled jobs")

    def shutdown(self) -> None:
        """Gracefully stop heartbeat thread."""
        self._running = False
        self._heartbeat_thread.join()
