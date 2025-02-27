# File Line Iterator in Python

This example demonstrates a file line iterator class in Python. This iterator allows you to read lines from a file one at a time, which is useful for processing large files without loading the entire content into memory.

## Code Implementation

<pre>class FileLineIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()  
        else:
            self.file.close()
            raise StopIteration

file_iterator = FileLineIterator('sample.txt')
for line in file_iterator:
    print(line)
    </pre>

## Explanation

The `FileLineIterator` class implements the iterator protocol to read lines from a file:

*   `__iter__()`: This method returns the iterator object itself, making it iterable.
*   `__next__()`: This method reads the next line from the file. If there are no more lines, it closes the file and raises a `StopIteration` exception.

## Approach to the Problem

The approach taken in this example is to create an iterator that reads lines from a specified file. This is particularly useful for handling large files where you want to process one line at a time without consuming too much memory.

## Why, What, and How

**Why:** Using an iterator for file reading allows for efficient memory usage and simplifies the process of reading large files.

**What:** This code defines a file line iterator that yields lines from a file until the end of the file is reached.

**How:** By implementing the `__iter__` and `__next__` methods, we enable the use of the iterator in a for loop, allowing for easy traversal of the file's lines.

<div class="note">**Note:** This example was created using Blackbox AI.</div>