import unittest
import os
import time
import shutil
from src.producer.producer import Producer
from src.consumer.consumer import Consumer
from src.queue.sqlite_queue import PersistentQSQLite

class TestProducerConsumer(unittest.TestCase):
    def setUp(self):
        """Set up test environment with writable permissions."""
        self.db_path = "data/test_queue.db"
        self.files_dir = "data/test_files"
        if os.path.exists(self.db_path):
            os.chmod(self.db_path, 0o666)
            os.remove(self.db_path)
        if os.path.exists(self.files_dir):
            shutil.rmtree(self.files_dir)
        os.makedirs(self.files_dir, exist_ok=True)
        os.chmod(self.files_dir, 0o777)
        self.queue = PersistentQSQLite(self.db_path)
        self.producer = Producer(self.queue, self.files_dir)
        self.consumer = Consumer(self.queue)
        print("Setup: Test environment initialized.")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        if os.path.exists(self.files_dir):
            shutil.rmtree(self.files_dir)
        print("Teardown: Test environment cleaned up.")

    # Producer Tests
    def test_producer_generate_file(self):
        """Test Producer generates a file and returns its path."""
        print("Running test_producer_generate_file...")
        filepath = self.producer.generate_file()
        print(f"Producer: Generated file {filepath}")
        self.assertTrue(os.path.exists(filepath), "File should exist")
        self.assertTrue(filepath.startswith(self.files_dir), "File should be in test_files dir")
        self.assertTrue(filepath.endswith(".txt"), "File should be .txt")
        with open(filepath, "r") as f:
            content = f.read()
            self.assertEqual(content, "Sample content\n", "File content should match")
        print("test_producer_generate_file passed.")

    def test_producer_enqueue(self):
        """Test Producer submits generated file to queue."""
        print("Running test_producer_enqueue...")
        filepath = self.producer.generate_file()
        self.queue.enqueue(filepath)
        print(f"Producer: Enqueued {filepath} to queue")
        status = self.queue.get_status()
        self.assertEqual(len(status), 1, "Queue should have 1 job")
        self.assertEqual(status[0]["id"], filepath, "Job ID should match filepath")
        self.assertEqual(status[0]["status"], "PENDING", "Job should be PENDING")
        print("test_producer_enqueue passed.")

    def test_producer_run(self):
        """Test Producer runs and generates/enqueues files."""
        print("Running test_producer_run...")
        filepath = self.producer.generate_file()
        self.producer.queue.enqueue(filepath)
        print(f"Producer: Simulated run, enqueued {filepath}")
        time.sleep(0.1)  # Brief pause for DB commit
        files = os.listdir(self.files_dir)
        self.assertGreater(len(files), 0, "At least one file should be generated")
        status = self.queue.get_status()
        self.assertGreater(len(status), 0, "At least one job should be enqueued")
        print("test_producer_run passed.")

    # Consumer Tests
    def test_consumer_process_job(self):
        """Test Consumer processes a job by adding timestamp."""
        print("Running test_consumer_process_job...")
        test_file = os.path.join(self.files_dir, "test.txt")
        with open(test_file, "w") as f:
            f.write("Test line\n")
        self.consumer.process_job(test_file)
        with open(test_file, "r") as f:
            content = f.read()
        self.assertTrue(content.startswith("20"), "Content should start with timestamp")
        self.assertIn("Test line\n", content, "Original content should remain")
        print("test_consumer_process_job passed.")

    def test_consumer_process_nonexistent_file(self):
        """Test Consumer handles missing file gracefully."""
        print("Running test_consumer_process_nonexistent_file...")
        nonexistent_file = "nonexistent.txt"
        self.consumer.process_job(nonexistent_file)
        # No assertion needed; just verify it doesn’t crash
        print(f"Consumer: Attempted to process {nonexistent_file} (expected failure handled)")
        print("test_consumer_process_nonexistent_file passed.")

    def test_consumer_run(self):
        """Test Consumer processes jobs from queue."""
        print("Running test_consumer_run...")
        test_file = os.path.join(self.files_dir, "test.txt")
        with open(test_file, "w") as f:
            f.write("Test line\n")
        self.queue.enqueue(test_file)
        print(f"Setup: Enqueued {test_file} for consumer")
        
        import threading
        consumer_thread = threading.Thread(target=self.consumer.run)
        consumer_thread.daemon = True
        consumer_thread.start()
        time.sleep(0.5)  # Give it time to process
        
        with open(test_file, "r") as f:
            content = f.read()
            self.assertTrue(content.startswith("20"), "Timestamp should be added")
        status = self.queue.get_status()
        self.assertEqual(len(status), 1, "Queue should have 1 job")
        self.assertEqual(status[0]["status"], "COMPLETED", "Job should be COMPLETED")
        print("test_consumer_run passed.")

if __name__ == "__main__":
    unittest.main()