# src/producer/producer.py
# Purpose: Generates unique file-based jobs and enqueues them

import logging
import os
import signal
import time
from uuid import uuid4

from dotenv import load_dotenv

from src.jobqueue import PersistentQInterface, get_queue

# Load environment variables
load_dotenv()
OUTPUT_DIR = os.getenv("JOBQUEUE_OUTPUT_DIR", "data/files")
LOG_DIR = os.getenv("JOBQUEUE_LOG_DIR", "logs")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=f"{LOG_DIR}/producer.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class Producer:
    """Generates and submits file-based jobs to the queue."""

    def __init__(self, queue: PersistentQInterface, output_dir: str = OUTPUT_DIR):
        """Initialize producer with queue and output directory."""
        self.queue = queue
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.running = True
        signal.signal(signal.SIGTERM, self._shutdown_signal)
        signal.signal(signal.SIGINT, self._shutdown_signal)

    def generate_file(self) -> str:
        """Generate a unique file job; return filepath or None on failure."""
        try:
            filename = f"{uuid4()}.txt"
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, "w") as f:
                f.write("Sample content\n")
            return filepath
        except Exception as e:
            logger.error(f"Failed to generate file: {e}")
            return None

    def run(self) -> None:
        """Run producer loop, submitting jobs every 5 seconds."""
        logger.info("Producer starting")
        while self.running:
            filepath = self.generate_file()
            if filepath:
                self.queue.enqueue(filepath)
                logger.info(f"Enqueued job: {filepath}")
            time.sleep(5)
        logger.info("Producer stopped")

    def _shutdown_signal(self, signum, frame) -> None:
        """Handle shutdown signals (SIGTERM, SIGINT) gracefully."""
        logger.info(f"Received signal {signum}, shutting down producer")
        self.running = False

if __name__ == "__main__":
    queue = get_queue()
    producer = Producer(queue)
    producer.run()
