import fileinput
from typing import Iterator

class FileRecords:
    def __init__(self, filename: str):
        if not isinstance(filename, str):
            raise TypeError("filename must be a string")
        self.filename = filename

    def __iter__(self) -> Iterator[str]:
        for line in fileinput.input(self.filename):
            yield line.strip()

def file_records(filename: str) -> Iterator[str]:
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    yield from FileRecords(filename)