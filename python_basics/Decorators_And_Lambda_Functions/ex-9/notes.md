<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Class Method Decorator Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-x: auto;
        }
        .content {
            margin-bottom: 20px;
        }
        .note {
            background-color: #e7f3fe;
            border-left: 6px solid #2196F3;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Python Class Method Decorator Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a decorator called <code>validate_args</code> that checks the arguments passed to a class method. If any argument is <code>None</code>, it raises a <code>ValueError</code>. The decorator is applied to the <code>add</code> method of the <code>Calculator</code> class to demonstrate its functionality.</p>
        
        <h3>Why?</h3>
        <p>Using decorators for argument validation helps ensure that methods receive valid inputs, which can prevent runtime errors and improve the robustness of the code.</p>
        
        <h3>What?</h3>
        <p>The <code>validate_args</code> decorator wraps the <code>add</code> method, checking if any of the provided arguments are <code>None</code> before executing the method.</p>
        
        <h3>How?</h3>
        <p>The decorator is defined as a function that takes another function as an argument. Inside the decorator, a wrapper function is defined that performs the validation and calls the original method if the validation passes.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
def validate_args(func):
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

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to implement a class method decorator in Python to validate arguments, ensuring that methods receive appropriate inputs.
    </div>

</body>
</html>