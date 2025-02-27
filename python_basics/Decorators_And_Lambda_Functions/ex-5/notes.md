# Python Debug Information Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `debug_info` that prints debug information about the function being called, including its name, arguments, keyword arguments, and the result it returns.

### Why?

Debugging decorators are useful for tracking the flow of data through functions, making it easier to understand how inputs are transformed into outputs. This can help identify issues in the code during development.

### What?

The `debug_info` decorator wraps the `add` function, logging the function's name, its arguments, and the result of the function call.

### How?

The decorator is defined as a function that takes another function as an argument. Inside the decorator, a wrapper function is defined that adds the debugging behavior and calls the original function.

</div>

## Python Code

<pre>def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}, Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@debug_info
def add(a, b):
    return a + b

# Example Usage
print(add(5, 10))  # Output: 15
    </pre>

<div class="note">**Note:** This code demonstrates how to create a debugging decorator in Python to log function calls and their results, which can be invaluable for troubleshooting and understanding code behavior.</div>
