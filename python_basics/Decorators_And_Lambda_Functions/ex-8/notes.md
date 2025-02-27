# Python Logging Decorator with Parameters Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `custom_logger` that takes a message as a parameter and logs the start and end of a function's execution. The decorator is applied to the `process_data` function to demonstrate its functionality.

### Why?

Logging decorators are useful for tracking the execution flow of functions, which can help in debugging and monitoring the behavior of applications. By allowing a custom message, the decorator can provide context for the logs.

### What?

The `custom_logger` decorator wraps the `process_data` function, printing a log message before and after the function's execution, along with the specified message.

### How?

The decorator is defined as a function that takes a message as an argument, which returns another function (the actual decorator). This inner function wraps the original function and adds the logging behavior.

</div>

## Python Code

<pre>def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - {func.__name__} started")  # Log start
            result = func(*args, **kwargs)  # Call the original function
            print(f"{message} - {func.__name__} ended")  # Log end
            return result
        return wrapper
    return decorator

@custom_logger("INFO")
def process_data():
    print("Processing data...")

# Example Usage
process_data()
    </pre>

<div class="note">**Note:** This code demonstrates how to create a logging decorator in Python that accepts parameters, allowing for customizable logging messages for different functions.</div>
