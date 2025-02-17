
from iterators import fibonacci  # Import the generator

fib = fibonacci()
for _ in range(10):  # Skip first 10
    next(fib)
for _ in range(10):  # Print next 10
    print(next(fib))