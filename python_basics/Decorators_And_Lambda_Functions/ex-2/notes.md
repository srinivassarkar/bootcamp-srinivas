# Python Decorator with Arguments Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `prefix_printer` that takes an argument (a prefix string) and prints the prefix along with the name of the function being called. The decorator is applied to the `say_hello` function to demonstrate its functionality.

### Why?

Decorators with arguments allow for more flexible and reusable decorators. In this case, the prefix can be customized for different functions, providing context for the log messages.

### What?

The `prefix_printer` decorator wraps the `say_hello` function, printing a log message that includes the specified prefix and the function's name before executing the function.

### How?

The decorator is defined as a function that takes a prefix as an argument, which returns another function (the actual decorator). This inner function wraps the original function and adds the desired behavior.

</div>

## Python Code

<pre>def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_printer("LOG:")
def say_hello():
    print("Hello!")

# Example Usage
say_hello()
    </pre>

<div class="note">**Note:** This code demonstrates how to create decorators in Python that accept arguments, allowing for more dynamic and customizable behavior.</div>