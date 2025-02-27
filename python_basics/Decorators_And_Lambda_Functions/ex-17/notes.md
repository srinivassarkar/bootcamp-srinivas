<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python LRU Cache Example</title>
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

    <h1>Python LRU Cache Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code demonstrates the use of the <code>functools.lru_cache</code> decorator to optimize the computation of the Fibonacci sequence. The <code>lru_cache</code> caches the results of function calls to improve performance, especially for recursive functions.</p>
        
        <h3>Why?</h3>
        <p>Recursive functions like Fibonacci can have exponential time complexity due to repeated calculations of the same values. Caching results significantly reduces the number of computations needed, making the function much more efficient.</p>
        
        <h3>What?</h3>
        <p>The <code>fibonacci</code> function is decorated with <code>@functools.lru_cache(maxsize=None)</code>, which allows it to store an unlimited number of results. When the function is called with the same argument, it retrieves the result from the cache instead of recalculating it.</p>
        
        <h3>How?</h3>
        <p>The <code>lru_cache</code> decorator is applied directly above the function definition. When the function is called, it checks if the result is already cached; if so, it returns the cached result, otherwise, it computes the result and stores it in the cache.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example Usage
print(fibonacci(20))  # Output: 6765
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use the <code>lru_cache</code> decorator in Python to optimize recursive functions, significantly improving performance for functions like Fibonacci.
    </div>

</body>
</html>