# src/jobqueue/sqlite_backend.py
"""SQLite-based persistent queue with robust crash recovery and thread safety."""

import logging
import os
import sqlite3
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from uuid import uuid4

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("JOBQUEUE_DB_PATH", "data/queue.db")
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(LOG_DIR, "jobqueue.log"),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class PersistentQSQLite:
    """SQLite-backed queue with persistent job storage and crash resilience."""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.consumer_id = str(uuid4())
        self._running = True
        self._lock = threading.Lock()
        self._init_db()
        self._heartbeat_thread = threading.Thread(target=self._run_heartbeat_check, daemon=True)
        self._heartbeat_thread.start()
        self._supports_returning = sqlite3.sqlite_version_info >= (3, 35, 0)  # Check SQLite version

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
        """Get a new SQLite connection per call—thread-safe with lock."""
        conn = sqlite3.connect(self.db_path, isolation_level=None)
        conn.row_factory = sqlite3.Row
        return conn

    def _run_heartbeat_check(self) -> None:
        """Check for stalled jobs every 10 seconds."""
        while self._running:
            try:
                with self._lock:
                    with self._get_conn() as conn:
                        self.check_stalled_jobs(conn.cursor())
                time.sleep(10)
            except Exception as e:
                logger.error(f"Heartbeat check failed: {e}")

    def enqueue(self, job_id: str) -> None:
        """Enqueue a job; reset duplicates to PENDING."""
        if len(job_id) > 2000:
            logger.error(f"Job ID too long: {job_id[:50]}...")
            raise ValueError("Job ID exceeds 2000 characters")
        now = datetime.now().isoformat()
        with self._lock:
            with self._get_conn() as conn:
                conn.execute(
                    """
                    INSERT INTO jobs (id, status, created_at, updated_at)
                    VALUES (?, 'PENDING', ?, ?)
                    ON CONFLICT(id) DO UPDATE SET status='PENDING', updated_at=excluded.updated_at
                """,
                    (job_id, now, now),
                )
        logger.info(f"Enqueued job_id: {job_id}")

    def dequeue(self) -> Optional[str]:
        """Dequeue a job atomically using transaction."""
        with self._lock:
            with self._get_conn() as conn:
                cursor = conn.cursor()
                cursor.execute("BEGIN IMMEDIATE")
                try:
                    now = datetime.now().isoformat()
                    if self._supports_returning:
                        # SQLite 3.35+ with RETURNING
                        cursor.execute(
                            """
                            UPDATE jobs
                            SET status = 'PROCESSING', consumer_id = ?, last_heartbeat = ?, updated_at = ?
                            WHERE id = (
                                SELECT id FROM jobs
                                WHERE status = 'PENDING'
                                ORDER BY created_at ASC
                                LIMIT 1
                            )
                            RETURNING id
                        """,
                            (self.consumer_id, now, now),
                        )
                        row = cursor.fetchone()
                        if row:
                            job_id = row["id"]
                            logger.info(f"Dequeued job_id: {job_id} by {self.consumer_id}")
                            conn.commit()
                            return job_id
                    else:
                        # Fallback for older SQLite
                        cursor.execute("""
                            SELECT id FROM jobs 
                            WHERE status = 'PENDING' 
                            ORDER BY created_at ASC 
                            LIMIT 1
                        """)
                        row = cursor.fetchone()
                        if row:
                            job_id = row["id"]
                            cursor.execute(
                                """
                                UPDATE jobs 
                                SET status = 'PROCESSING', consumer_id = ?, last_heartbeat = ?, updated_at = ?
                                WHERE id = ? AND status = 'PENDING'
                            """,
                                (self.consumer_id, now, now, job_id),
                            )
                            if cursor.rowcount == 0:
                                raise sqlite3.IntegrityError("Job already taken")
                            logger.info(f"Dequeued job_id: {job_id} by {self.consumer_id}")
                            conn.commit()
                            return job_id
                    conn.commit()
                    return None
                except Exception as e:
                    conn.rollback()
                    logger.error(f"Dequeue failed: {e}")
                    return None

    def heartbeat(self) -> None:
        """Update heartbeat for PROCESSING jobs owned by this consumer."""
        now = datetime.now().isoformat()
        with self._lock:
            with self._get_conn() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    UPDATE jobs 
                    SET last_heartbeat = ? 
                    WHERE consumer_id = ? AND status = 'PROCESSING'
                """,
                    (now, self.consumer_id),
                )
                if cursor.rowcount > 0:
                    logger.debug(f"Heartbeat updated for {self.consumer_id}")

    def complete(self, job_id: str) -> None:
        """Mark job as COMPLETED if owned by this consumer."""
        now = datetime.now().isoformat()
        with self._lock:
            with self._get_conn() as conn:
                conn.execute(
                    """
                    UPDATE jobs 
                    SET status = 'COMPLETED', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
                    WHERE id = ? AND consumer_id = ?
                """,
                    (now, job_id, self.consumer_id),
                )
        logger.info(f"Completed job_id: {job_id} by {self.consumer_id}")

    def mark_failed(self, job_id: str) -> None:
        """Mark job as FAILED or UNPROCESSABLE based on retries, reset to PENDING if retryable."""
        now = datetime.now().isoformat()
        with self._lock:
            with self._get_conn() as conn:
                cursor = conn.cursor()
                # Increment retries
                cursor.execute(
                    """
                    UPDATE jobs 
                    SET retries = retries + 1, updated_at = ?
                    WHERE id = ? AND consumer_id = ? AND status = 'PROCESSING'
                """,
                    (now, job_id, self.consumer_id),
                )
                if cursor.rowcount == 0:
                    logger.warning(
                        f"Job {job_id} not found or not PROCESSING for {self.consumer_id}"
                    )
                    return
                # Check retries and reset or mark final
                cursor.execute("SELECT retries FROM jobs WHERE id = ?", (job_id,))
                retries = cursor.fetchone()["retries"]
                if retries < 3:
                    cursor.execute(
                        """
                        UPDATE jobs 
                        SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
                        WHERE id = ?
                    """,
                        (now, job_id),
                    )
                    logger.info(f"Job {job_id} failed, retries={retries}, reset to PENDING")
                else:
                    cursor.execute(
                        """
                        UPDATE jobs 
                        SET status = 'UNPROCESSABLE', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
                        WHERE id = ?
                    """,
                        (now, job_id),
                    )
                    logger.warning(f"Job {job_id} failed, retries={retries}, marked UNPROCESSABLE")

    def get_status(self) -> List[Dict[str, str]]:
        """Retrieve all job statuses."""
        with self._lock:
            with self._get_conn() as conn:
                return [dict(row) for row in conn.execute("SELECT * FROM jobs")]

    def resubmit(self, job_id: str) -> None:
        """Reset FAILED job to PENDING."""
        now = datetime.now().isoformat()
        with self._lock:
            with self._get_conn() as conn:
                conn.execute(
                    """
                    UPDATE jobs 
                    SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
                    WHERE id = ? AND status = 'FAILED'
                """,
                    (now, job_id),
                )
        logger.info(f"Resubmitted job_id: {job_id}")

    def cancel(self, job_id: str) -> None:
        """Mark job as CANCELED if allowed."""
        now = datetime.now().isoformat()
        with self._lock:
            with self._get_conn() as conn:
                conn.execute(
                    """
                    UPDATE jobs 
                    SET status = 'CANCELED', updated_at = ?
                    WHERE id = ? AND status IN ('PENDING', 'FAILED', 'UNPROCESSABLE')
                """,
                    (now, job_id),
                )
        logger.info(f"Canceled job_id: {job_id}")

    def check_stalled_jobs(self, cursor: Optional[sqlite3.Cursor] = None) -> None:
        """Requeue stalled PROCESSING jobs with NULL or old heartbeat."""
        now = datetime.now().isoformat()
        cursor = cursor or self._get_conn().cursor()
        cursor.execute(
            """
            UPDATE jobs 
            SET status = 'PENDING', consumer_id = NULL, last_heartbeat = NULL, updated_at = ?
            WHERE status = 'PROCESSING' 
            AND (last_heartbeat IS NULL OR last_heartbeat < ?)
        """,
            (now, (datetime.now() - timedelta(seconds=30)).isoformat()),
        )
        logger.info("Checked and requeued stalled jobs")

    def shutdown(self) -> None:
        """Gracefully stop heartbeat thread."""
        self._running = False
        self._heartbeat_thread.join()
