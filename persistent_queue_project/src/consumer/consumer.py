# src/consumer/consumer.py
"""Consumer processing jobs from the queue with crash resilience."""

import logging
import os
import random
import signal
import time
from datetime import datetime

from dotenv import load_dotenv

from src.jobqueue import PersistentQInterface, get_queue

load_dotenv()
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

logging.basicConfig(
    level=logging.INFO,
    filename=f"{LOG_DIR}/consumer.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class Consumer:
    """Processes file jobs from queue, updates with timestamps."""

    def __init__(self):
        self.queue: PersistentQInterface = get_queue()
        self.running = True
        signal.signal(signal.SIGTERM, self._shutdown_signal)
        signal.signal(signal.SIGINT, self._shutdown_signal)

    def process_job(self, job_id: str) -> None:
        """Process a job by appending timestamps; handle failures."""
        try:
            if not os.path.exists(job_id):
                raise FileNotFoundError(f"Job file {job_id} not found")
            with open(job_id, "r") as f:
                lines = f.readlines()
            with open(job_id, "w") as f:
                for line in lines:
                    f.write(f"{datetime.now().isoformat()} - {line}")
            self.queue.complete(job_id)
            logger.info(f"Processed job_id: {job_id} by {self.queue.consumer_id}")
        except Exception as e:
            logger.error(f"Failed job_id {job_id}: {e}")
            self.queue.mark_failed(job_id)
            raise  # Ensure heartbeat doesn’t mask failure

    def run(self) -> None:
        """Run consumer loop with randomized delay."""
        logger.info(f"Consumer {self.queue.consumer_id} starting")
        while self.running:
            try:
                job_id = self.queue.dequeue()
                if job_id:
                    self.process_job(job_id)
                    self.queue.heartbeat()  # Periodic ping
                time.sleep(random.uniform(7, 15))
            except Exception as e:
                logger.error(f"Consumer run error: {e}")
                time.sleep(1)  # Backoff on error
        logger.info(f"Consumer {self.queue.consumer_id} stopped")
        self.queue.shutdown()

    def _shutdown_signal(self, signum, frame) -> None:
        """Handle shutdown signals gracefully."""
        logger.info(f"Consumer {self.queue.consumer_id} received signal {signum}, shutting down")
        self.running = False

if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()