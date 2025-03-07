import logging
import os
import random
import re
import signal
import threading
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv

from src.jobqueue import PersistentQInterface, get_queue

load_dotenv()
LOG_DIR = os.getenv(
    "JOBQUEUE_LOG_DIR", os.path.join(os.path.expanduser("~"), "persistent_queue_logs")
)
os.makedirs(LOG_DIR, exist_ok=True)


class Consumer:
    def __init__(self):
        self.queue: PersistentQInterface = get_queue()
        self.running = True
        self.draining = False
        self.shutdown_event = threading.Event()
        self.logger = logging.getLogger(f"consumer.{self.queue.consumer_id}")
        self.logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(
            f"{LOG_DIR}/consumer_{self.queue.consumer_id}.log",
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
        )
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(handler)
        # Configurable regex for job_id validation
        self.job_id_pattern = os.getenv("JOB_ID_PATTERN", r"^data/files/[a-f0-9-]+\.txt$")
        signal.signal(signal.SIGTERM, self._shutdown_signal)
        signal.signal(signal.SIGINT, self._shutdown_signal)

    def process_job(self, job_id: str, max_retries: int = 3) -> None:
        """Process a job with retries and periodic heartbeats."""
        if not re.match(self.job_id_pattern, job_id):
            self.logger.error(f"Invalid job_id format: {job_id}")
            self.queue.mark_failed(job_id)
            return

        attempt = 0
        base_delay = 1  # Seconds
        while attempt < max_retries:
            try:
                if not os.path.exists(job_id):
                    raise FileNotFoundError(f"Job file {job_id} not found")

                # Simulate long-running job with periodic heartbeats
                with open(job_id, "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    time.sleep(0.5)  # Simulate work
                    if i % 2 == 0:  # Every ~1s
                        self.queue.heartbeat()
                        self.logger.debug(f"Heartbeat sent during {job_id} processing")
                    with open(job_id, "w") as f:
                        f.write(f"{datetime.now().isoformat()} - {line}")

                self.queue.complete(job_id)
                self.logger.info(f"Processed job_id: {job_id} by {self.queue.consumer_id}")
                return  # Success, exit
            except Exception as e:
                attempt += 1
                self.logger.error(f"Attempt {attempt}/{max_retries} failed for {job_id}: {e}")
                if attempt == max_retries:
                    self.queue.mark_failed(job_id)
                    self.logger.warning(f"Max retries reached for {job_id}, marked failed")
                else:
                    # Exponential backoff: 1s, 2s, 4s...
                    delay = base_delay * (2 ** (attempt - 1))
                    self.logger.info(f"Retrying {job_id} in {delay}s")
                    time.sleep(delay)

    def run(self) -> None:
        """Run consumer loop with thread-safe dequeue and dynamic backoff."""
        self.logger.info(f"Consumer {self.queue.consumer_id} starting")
        base_backoff = 0.5  # Initial sleep when queue empty
        max_backoff = 8.0  # Cap backoff at 8s
        backoff = base_backoff

        while self.running:
            # Thread-safe dequeue—relies on sqlite_backend.py's lock
            job_id = self.queue.dequeue()
            if job_id:
                try:
                    self.logger.info(f"Dequeued job_id: {job_id}")
                    self.process_job(job_id)
                    self.queue.heartbeat()
                    backoff = base_backoff  # Reset backoff on success
                except Exception as e:
                    self.logger.error(f"Consumer run error on job {job_id}: {e}")
                time.sleep(random.uniform(1, 3))  # Normal processing delay
            else:
                self.logger.debug("No jobs to dequeue—queue empty or locked")
                time.sleep(backoff)
                # Exponential backoff when idle: 0.5s, 1s, 2s, 4s, 8s...
                backoff = min(max_backoff, backoff * 2)

        self.logger.info(f"Consumer {self.queue.consumer_id} shutting down—draining queue")
        self.draining = True
        while self.draining and not self.shutdown_event.is_set():
            job_id = self.queue.dequeue()
            if not job_id:
                break
            try:
                self.logger.info(f"Dequeued job_id: {job_id} during drain")
                self.process_job(job_id)
            except Exception as e:
                self.logger.error(f"Drain error on job {job_id}: {e}")
        self.logger.info(f"Consumer {self.queue.consumer_id} stopped")
        self.queue.shutdown()

    def _shutdown_signal(self, signum, frame) -> None:
        """Handle shutdown signals gracefully across threads."""
        self.logger.info(
            f"Consumer {self.queue.consumer_id} received signal {signum}, shutting down"
        )
        self.running = False
        self.draining = True
        self.shutdown_event.set()
        # Ensure heartbeat thread in sqlite_backend.py stops
        self.queue.shutdown()


if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()
