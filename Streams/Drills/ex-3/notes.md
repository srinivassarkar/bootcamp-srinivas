# File Line Generator in Python

This example demonstrates a generator function in Python that reads lines from a file. Generators are a more concise and memory-efficient way to produce values one at a time compared to custom iterator classes.

## Code Implementation

<pre>def file_line_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Using the generator
for line in file_line_generator('sample.txt'):
    print(line)
    </pre>

## Explanation

The `file_line_generator` function is a generator that yields lines from a specified file:

*   `yield`: This keyword is used to produce a value and pause the function's execution, allowing it to be resumed later. This makes the function a generator.
*   `with open(filename, 'r')`: This context manager ensures that the file is properly opened and closed, even if an error occurs.

## Approach to the Problem

The approach taken in this example is to create a generator that reads lines from a specified file. This is particularly useful for handling large files where you want to process one line at a time without consuming too much memory.

## Why, What, and How

**Why:** Generators are simpler to write and more memory-efficient for large datasets, making them a preferred choice for many applications.

**What:** This code defines a generator function that yields lines from a file until the end of the file is reached.

**How:** By using the `yield` keyword, we enable the function to produce values one at a time, allowing for easy traversal of the file's lines in a for loop.

<div class="note">**Note:** This example was created using Blackbox AI.</div>