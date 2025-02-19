from typing import Iterator

class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def fibonacci() -> Iterator[int]:
    fib = Fibonacci()
    yield from fib