# src/producer/producer.py
"""Producer generating file-based jobs for the queue."""

import logging
import os
import signal
import time
from datetime import datetime
from uuid import uuid4

from dotenv import load_dotenv

from src.jobqueue import PersistentQInterface, get_queue

load_dotenv()
OUTPUT_DIR = os.getenv("JOBQUEUE_OUTPUT_DIR", "data/files")
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

logging.basicConfig(
    level=logging.INFO,
    filename=f"{LOG_DIR}/producer.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class Producer:
    """Generates unique file jobs and enqueues them every 5 seconds."""

    def __init__(self, queue: PersistentQInterface, output_dir: str = OUTPUT_DIR):
        self.queue = queue
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.running = True
        signal.signal(signal.SIGTERM, self._shutdown_signal)
        signal.signal(signal.SIGINT, self._shutdown_signal)

    def generate_file(self) -> str:
        """Generate a job file and return its ID."""
        job_id = f"data/files/{uuid4()}.txt"
        # Optional: Validate against JOB_ID_PATTERN
        import re

        pattern = os.getenv("JOB_ID_PATTERN", r"^data/files/[a-f0-9-]+\.txt$")
        if not re.match(pattern, job_id):
            raise ValueError(f"Generated job_id {job_id} doesn’t match pattern {pattern}")
        os.makedirs("data/files", exist_ok=True)
        with open(job_id, "w") as f:
            f.write(f"Job created at {datetime.now().isoformat()}\n")
        return job_id

    def run(self) -> None:
        """Run producer loop, enqueuing jobs every 5 seconds."""
        logger.info("Producer starting")
        while self.running:
            try:
                job_id = self.generate_file()
                self.queue.enqueue(job_id)
                logger.info(f"Enqueued job_id: {job_id}")  # Only log here
                time.sleep(5)
            except Exception as e:
                logger.error(f"Producer run error: {e}")
                time.sleep(1)
        logger.info("Producer stopped")

    def _shutdown_signal(self, signum, frame) -> None:
        """Handle shutdown signals gracefully."""
        logger.info(f"Producer received signal {signum}, shutting down")
        self.running = False


if __name__ == "__main__":
    queue = get_queue()
    producer = Producer(queue)
    producer.run()
