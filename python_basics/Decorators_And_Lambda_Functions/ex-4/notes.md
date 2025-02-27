# Python Memoization Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `memoize` that caches the results of function calls to optimize performance, particularly for recursive functions like `fibonacci`.

### Why?

Memoization is a technique used to speed up function execution by storing previously computed results. This is especially useful for functions with overlapping subproblems, such as the Fibonacci sequence.

### What?

The `memoize` decorator wraps the `fibonacci` function, caching results based on the input arguments. If the function is called with the same arguments again, it returns the cached result instead of recalculating it.

### How?

The decorator maintains a cache (a dictionary) that stores results. When the wrapped function is called, it checks if the result is already in the cache. If it is, it returns the cached result; otherwise, it computes the result, stores it in the cache, and then returns it.

</div>

## Python Code

<pre>def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]  # Return cached result if available
        result = func(*args)  # Compute the result
        cache[args] = result  # Store the result in cache
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example Usage
print(fibonacci(10))  # Output: 55
    </pre>

<div class="note">**Note:** This code demonstrates how to implement a memoization decorator in Python to optimize recursive functions, significantly improving performance for functions like Fibonacci.</div>