# Python Class Method Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `validate_args` that checks the arguments passed to a class method. If any argument is `None`, it raises a `ValueError`. The decorator is applied to the `add` method of the `Calculator` class to demonstrate its functionality.

### Why?

Using decorators for argument validation helps ensure that methods receive valid inputs, which can prevent runtime errors and improve the robustness of the code.

### What?

The `validate_args` decorator wraps the `add` method, checking if any of the provided arguments are `None` before executing the method.

### How?

The decorator is defined as a function that takes another function as an argument. Inside the decorator, a wrapper function is defined that performs the validation and calls the original method if the validation passes.

</div>

## Python Code

<pre>def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if any(arg is None for arg in args):  # Check for None arguments
            raise ValueError("Arguments cannot be None")
        return func(self, *args, **kwargs)  # Call the original method
    return wrapper

class Calculator:
    @validate_args
    def add(self, a, b):
        return a + b

# Example Usage
calc = Calculator()
print(calc.add(10, 20))  # Output: 30
    </pre>

<div class="note">**Note:** This code demonstrates how to implement a class method decorator in Python to validate arguments, ensuring that methods receive appropriate inputs.</div>