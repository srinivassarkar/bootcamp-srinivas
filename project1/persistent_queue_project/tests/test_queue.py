import unittest
import os
import time
import sqlite3
from src.queue.sqlite_queue import PersistentQSQLite

class TestPersistentQueue(unittest.TestCase):
    def setUp(self):
        """Set up a fresh queue for each test."""
        self.db_path = "data/test_queue.db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.queue = PersistentQSQLite(self.db_path)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_enqueue(self):
        """Test adding a job to the queue."""
        job_id = "test_job_1"
        self.queue.enqueue(job_id)
        status = self.queue.get_status()
        self.assertEqual(len(status), 1)
        self.assertEqual(status[0]["id"], job_id)
        self.assertEqual(status[0]["status"], "PENDING")

    def test_enqueue_too_long(self):
        """Test enqueue fails for job > 2000 chars."""
        long_job = "a" * 2001
        with self.assertRaises(ValueError):
            self.queue.enqueue(long_job)

    def test_dequeue(self):
        """Test dequeue retrieves a job and marks it PROCESSING."""
        job_id = "test_job_2"
        self.queue.enqueue(job_id)
        dequeued_job = self.queue.dequeue()
        self.assertEqual(dequeued_job, job_id)
        status = self.queue.get_status()
        self.assertEqual(status[0]["status"], "PROCESSING")

    def test_dequeue_empty(self):
        """Test dequeue returns None when queue is empty."""
        self.assertIsNone(self.queue.dequeue())

    def test_complete(self):
        """Test completing a job updates its status."""
        job_id = "test_job_3"
        self.queue.enqueue(job_id)
        self.queue.dequeue()  # Mark as PROCESSING
        self.queue.complete(job_id)
        status = self.queue.get_status()
        self.assertEqual(status[0]["status"], "COMPLETED")

    def test_persistence(self):
        """Test queue persists across instances."""
        job_id = "test_job_4"
        self.queue.enqueue(job_id)
        del self.queue  # Close original queue
        new_queue = PersistentQSQLite(self.db_path)
        status = new_queue.get_status()
        self.assertEqual(len(status), 1)
        self.assertEqual(status[0]["id"], job_id)
        self.assertEqual(status[0]["status"], "PENDING")

    def test_concurrent_dequeue(self):
        """Test only one consumer can dequeue a job."""
        job_id = "test_job_5"
        self.queue.enqueue(job_id)
        # Simulate two consumers
        job1 = self.queue.dequeue()
        job2 = self.queue.dequeue()
        self.assertEqual(job1, job_id)
        self.assertIsNone(job2)  # Second dequeue should get nothing

    def test_resubmit(self):
        """Test resubmitting a failed job."""
        job_id = "test_job_6"
        self.queue.enqueue(job_id)
        self.queue.dequeue()  # Mark as PROCESSING
        # Simulate failure by manually setting to FAILED
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("UPDATE jobs SET status = 'FAILED' WHERE id = ?", (job_id,))
            conn.commit()
        self.queue.resubmit(job_id)
        status = self.queue.get_status()
        self.assertEqual(status[0]["status"], "PENDING")

    def test_cancel(self):
        """Test canceling a pending job."""
        job_id = "test_job_7"
        self.queue.enqueue(job_id)
        self.queue.cancel(job_id)
        status = self.queue.get_status()
        self.assertEqual(len(status), 0)

if __name__ == "__main__":
    unittest.main()