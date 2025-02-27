# Python Retry Mechanism Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `retry` that attempts to execute a function multiple times if it raises an exception. The decorator is applied to the `error_prone` function to demonstrate its functionality.

### Why?

Retry mechanisms are useful for handling transient errors, such as network issues or temporary unavailability of resources. By retrying a function, you can increase the chances of successful execution without requiring manual intervention.

### What?

The `retry` decorator wraps the `error_prone` function, allowing it to be called multiple times if it raises an exception. If the function fails after the specified number of retries, a message is printed indicating that the maximum retries have been reached.

### How?

The decorator is defined as a function that takes the number of retries as an argument, which returns another function (the actual decorator). This inner function wraps the original function and implements the retry logic.

</div>

## Python Code

<pre>def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)  # Attempt to call the function
                except Exception as e:
                    print(f"Error: {e}, Retrying...")  # Print error and retry
            print("Max retries reached")  # Print message if max retries reached
        return wrapper
    return decorator

@retry(3)
def error_prone():
    raise ValueError("Oops!")  # Simulate an error

# Example Usage
error_prone()  # This will attempt to call the function 3 times
    </pre>

<div class="note">**Note:** This code demonstrates how to implement a retry mechanism in Python using decorators, allowing functions to be retried automatically upon failure.</div>
