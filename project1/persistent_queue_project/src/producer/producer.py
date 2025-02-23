import os
import time
import random
import string
from src.queue.sqlite_queue import PersistentQSQLite

class Producer:
    def __init__(self, queue: PersistentQSQLite, output_dir: str = "data/files"):
        self.queue = queue
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_file(self) -> str:
        filename = ''.join(random.choices(string.ascii_letters, k=10)) + ".txt"
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "w") as f:
            f.write("Sample content\n")
        return filepath

    def run(self) -> None:
        while True:
            filepath = self.generate_file()
            print(f"Producer: Submitting {filepath}")
            self.queue.enqueue(filepath)
            time.sleep(5)

if __name__ == "__main__":
    queue = PersistentQSQLite()
    producer = Producer(queue)
    producer.run()