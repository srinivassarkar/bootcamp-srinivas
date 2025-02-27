<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Decorator Example</title>
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

    <h1>Python Decorator Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a decorator called <code>simple_logger</code> that logs messages before and after the execution of a function. The decorator is applied to the <code>greet</code> function to demonstrate its functionality.</p>
        
        <h3>Why?</h3>
        <p>Decorators provide a convenient way to modify or enhance the behavior of functions without changing their code. In this case, the decorator adds logging functionality to track when a function starts and ends.</p>
        
        <h3>What?</h3>
        <p>The <code>simple_logger</code> decorator wraps the <code>greet</code> function, printing messages to indicate the start and end of the function's execution.</p>
        
        <h3>How?</h3>
        <p>The decorator is defined as a function that takes another function as an argument. Inside the decorator, a wrapper function is defined that adds the logging behavior and calls the original function.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
def simple_logger(func):
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

    <div class="note">
        <strong>Note:</strong> This code demonstrates the use of decorators in Python to enhance function behavior, such as logging, without modifying the original function's code.
    </div>

</body>
</html>