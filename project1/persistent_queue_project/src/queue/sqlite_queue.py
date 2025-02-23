import sqlite3
from typing import List, Dict, Optional
from datetime import datetime
from .interface import PersistentQInterface

class PersistentQSQLite(PersistentQInterface):
    def __init__(self, db_path: str = "data/queue.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            conn.commit()

    def enqueue(self, job: str) -> None:
        if len(job) > 2000:
            raise ValueError("Job ID exceeds 2000 characters")
        now = datetime.now().isoformat()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR IGNORE INTO jobs (id, status, created_at, updated_at) VALUES (?, ?, ?, ?)",
                (job, "PENDING", now, now)
            )
            conn.commit()

    def dequeue(self) -> Optional[str]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            # Atomic update to mark job as PROCESSING
            cursor.execute("""
                UPDATE jobs 
                SET status = 'PROCESSING', updated_at = ?
                WHERE id = (
                    SELECT id FROM jobs WHERE status = 'PENDING' LIMIT 1
                )
                RETURNING id
            """, (datetime.now().isoformat(),))
            row = cursor.fetchone()
            conn.commit()
            return row["id"] if row else None

    def complete(self, job_id: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE jobs SET status = 'COMPLETED', updated_at = ? WHERE id = ? AND status = 'PROCESSING'",
                (datetime.now().isoformat(), job_id)
            )
            conn.commit()

    def get_status(self) -> List[Dict[str, str]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM jobs")
            return [dict(row) for row in cursor.fetchall()]

    def resubmit(self, job_id: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE jobs SET status = 'PENDING', updated_at = ? WHERE id = ? AND status = 'FAILED'",
                (datetime.now().isoformat(), job_id)
            )
            conn.commit()

    def cancel(self, job_id: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM jobs WHERE id = ? AND status IN ('PENDING', 'FAILED')",
                (job_id,)
            )
            conn.commit()