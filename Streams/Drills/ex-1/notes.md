# Simple Iterator in Python

This example demonstrates a simple iterator class in Python. Iterators are a fundamental concept in Python that allow you to traverse through a collection of items without needing to know the underlying structure.

## Code Implementation

<pre>class SimpleIterator:
    def __init__(self):
        self.current = 1
        self.end = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration  

iterator = SimpleIterator()
for number in iterator:
    print(number)
    </pre>

## Explanation

The `SimpleIterator` class implements the iterator protocol, which consists of two methods:

*   `__iter__()`: This method returns the iterator object itself. It is required to make the object iterable.
*   `__next__()`: This method returns the next value in the sequence. When there are no more items to return, it raises a `StopIteration` exception to signal that the iteration is complete.

## Approach to the Problem

The approach taken in this example is to create a simple iterator that generates numbers from 1 to 10\. This is useful for understanding how iterators work in Python and can be extended to more complex data structures.

## Why, What, and How

**Why:** Understanding iterators is crucial for working with collections in Python, as they provide a consistent way to access elements.

**What:** This code defines a simple iterator that yields numbers sequentially.

**How:** By implementing the `__iter__` and `__next__` methods, we enable the use of the iterator in a for loop, allowing for easy traversal of the number sequence.

<div class="note">**Note:** This example was created using Blackbox AI.</div>