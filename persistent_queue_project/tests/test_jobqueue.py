# tests/test_jobqueue.py
# Purpose: Unit tests for job queue functionality

import os
import sqlite3
from datetime import datetime, timedelta

import pytest

from src.jobqueue.sqlite_backend import PersistentQSQLite


@pytest.fixture
def queue(tmp_path):
    """Setup temporary SQLite queue for testing."""
    db_path = str(tmp_path / "test_queue.db")
    q = PersistentQSQLite(db_path)
    yield q
    if os.path.exists(db_path):
        os.remove(db_path)

def test_enqueue(queue: PersistentQSQLite):
    """Test job enqueuing."""
    queue.enqueue("job1")
    with sqlite3.connect(queue.db_path) as conn:
        row = conn.execute("SELECT * FROM jobs WHERE id = 'job1'").fetchone()
    assert row[0] == "job1" and row[1] == "PENDING"

def test_enqueue_max_length(queue: PersistentQSQLite):
    """Test job ID length validation."""
    with pytest.raises(ValueError, match="Job ID exceeds 2000 characters"):
        queue.enqueue("a" * 2001)

def test_dequeue(queue: PersistentQSQLite):
    """Test job dequeuing."""
    queue.enqueue("job1")
    assert queue.dequeue() == "job1"
