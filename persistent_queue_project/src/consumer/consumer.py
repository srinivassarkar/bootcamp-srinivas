# src/consumer/consumer.py
# Purpose: Consumes and processes jobs from the queue

import logging
import os
import random
import signal
import time
from datetime import datetime

from src.jobqueue import PersistentQInterface, get_queue

# Load environment variables
load_dotenv()
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=f"{LOG_DIR}/consumer.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class Consumer:
    """Processes jobs from the queue with failure and crash handling."""

    def __init__(self):
        """Initialize consumer with queue instance."""
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
            logger.info(f"Processed job: {job_id} by {self.queue.consumer_id}")
        except FileNotFoundError as e:
            logger.warning(f"Job {job_id} missing, marking complete: {e}")
            self.queue.complete(job_id)
        except Exception as e:
            logger.error(f"Failed to process job {job_id}: {e}")
            self.queue.mark_failed(job_id)

    def run(self) -> None:
        """Run consumer loop with random processing delays."""
        logger.info(f"Consumer {self.queue.consumer_id} starting")
        while self.running:
            try:
                job_id = self.queue.dequeue()
                if job_id:
                    self.process_job(job_id)
                    self.queue.heartbeat()
                time.sleep(random.uniform(7, 15))
            except Exception as e:
                logger.error(f"Consumer run loop error: {e}")
                time.sleep(1)  # Prevent tight loop on failure
        logger.info(f"Consumer {self.queue.consumer_id} stopped")

    def _shutdown_signal(self, signum, frame) -> None:
        """Handle shutdown signals (SIGTERM, SIGINT) gracefully."""
        logger.info(f"Consumer {self.queue.consumer_id} received signal {signum}, shutting down")
        self.running = False

if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()
