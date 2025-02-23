import time
import random
from datetime import datetime
# from typing import Optional
from src.queue.sqlite_queue import PersistentQSQLite

class Consumer:
    def __init__(self, queue: PersistentQSQLite):
        self.queue = queue

    def process_job(self, job_id: str) -> None:
        try:
            with open(job_id, "r") as f:
                lines = f.readlines()
            with open(job_id, "w") as f:
                for line in lines:
                    f.write(f"{datetime.now().isoformat()} - {line}")
            self.queue.complete(job_id)
            print(f"Consumer: Processed {job_id}")
        except Exception as e:
            print(f"Consumer: Failed {job_id} - {e}")
            # Mark as FAILED in a real system; here we just skip

    def run(self) -> None:
        while True:
            job_id = self.queue.dequeue()
            if job_id:
                self.process_job(job_id)
            time.sleep(random.uniform(7, 15))

if __name__ == "__main__":
    queue = PersistentQSQLite()
    consumer = Consumer(queue)
    consumer.run()