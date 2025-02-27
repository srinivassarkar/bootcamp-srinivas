# Python LRU Cache Example

<div class="content">

## Problem Approach

This Python code demonstrates the use of the `functools.lru_cache` decorator to optimize the computation of the Fibonacci sequence. The `lru_cache` caches the results of function calls to improve performance, especially for recursive functions.

### Why?

Recursive functions like Fibonacci can have exponential time complexity due to repeated calculations of the same values. Caching results significantly reduces the number of computations needed, making the function much more efficient.

### What?

The `fibonacci` function is decorated with `@functools.lru_cache(maxsize=None)`, which allows it to store an unlimited number of results. When the function is called with the same argument, it retrieves the result from the cache instead of recalculating it.

### How?

The `lru_cache` decorator is applied directly above the function definition. When the function is called, it checks if the result is already cached; if so, it returns the cached result, otherwise, it computes the result and stores it in the cache.
