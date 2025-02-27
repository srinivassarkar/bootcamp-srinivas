<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Retry Mechanism Decorator Example</title>
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

    <h1>Python Retry Mechanism Decorator Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a decorator called <code>retry</code> that attempts to execute a function multiple times if it raises an exception. The decorator is applied to the <code>error_prone</code> function to demonstrate its functionality.</p>
        
        <h3>Why?</h3>
        <p>Retry mechanisms are useful for handling transient errors, such as network issues or temporary unavailability of resources. By retrying a function, you can increase the chances of successful execution without requiring manual intervention.</p>
        
        <h3>What?</h3>
        <p>The <code>retry</code> decorator wraps the <code>error_prone</code> function, allowing it to be called multiple times if it raises an exception. If the function fails after the specified number of retries, a message is printed indicating that the maximum retries have been reached.</p>
        
        <h3>How?</h3>
        <p>The decorator is defined as a function that takes the number of retries as an argument, which returns another function (the actual decorator). This inner function wraps the original function and implements the retry logic.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
def retry(times):
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

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to implement a retry mechanism in Python using decorators, allowing functions to be retried automatically upon failure.
    </div>

</body>
</html>