# Python Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `simple_logger` that logs messages before and after the execution of a function. The decorator is applied to the `greet` function to demonstrate its functionality.

### Why?

Decorators provide a convenient way to modify or enhance the behavior of functions without changing their code. In this case, the decorator adds logging functionality to track when a function starts and ends.

### What?

The `simple_logger` decorator wraps the `greet` function, printing messages to indicate the start and end of the function's execution.

### How?

The decorator is defined as a function that takes another function as an argument. Inside the decorator, a wrapper function is defined that adds the logging behavior and calls the original function.

</div>

## Python Code

<pre>def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@simple_logger
def greet(name):
    print(f"Hello, {name}!")

# Example Usage
greet("Bunny")
    </pre>

<div class="note">**Note:** This code demonstrates the use of decorators in Python to enhance function behavior, such as logging, without modifying the original function's code.</div>
