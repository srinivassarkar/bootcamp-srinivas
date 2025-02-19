from typing import Iterator

class StringRange:
    def __init__(self, n: int):
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        self.n = n
        self.current = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.current >= self.n:
            raise StopIteration
        result = f"line number {self.current}"
        self.current += 1
        return result

def str_range(n: int) -> Iterator[str]:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    yield from StringRange(n)