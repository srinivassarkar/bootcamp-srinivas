# Python Timing Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `timer` that measures the execution time of a function. The decorator is applied to the `slow_function` to demonstrate its functionality.

### Why?

Timing decorators are useful for performance monitoring and optimization. They allow developers to easily measure how long a function takes to execute, which can help identify bottlenecks in the code.

### What?

The `timer` decorator wraps the `slow_function`, recording the start and end times of the function's execution and printing the total execution time.

### How?

The decorator is defined as a function that takes another function as an argument. Inside the decorator, a wrapper function is defined that adds the timing behavior and calls the original function.

</div>

## Python Code

<pre>import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end = time.time()  # Record the end time
        print(f"Execution time: {end - start:.4f} seconds")  # Print the execution time
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)  # Simulate a slow operation
    print("Function executed!")

# Example Usage
slow_function()
    </pre>

<div class="note">**Note:** This code demonstrates how to create a timing decorator in Python to measure the execution time of functions, which is useful for performance analysis.</div>