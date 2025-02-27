# Python Multiple Decorators Example

<div class="content">

## Problem Approach

This Python code demonstrates the use of multiple decorators to enhance the functionality of functions. The decorators include a simple logger, a timer, and a debug information logger.

### Why?

Using decorators allows for the separation of concerns, enabling you to add functionality such as logging, timing, and debugging without modifying the original function code. This promotes code reusability and maintainability.

### What?

The code defines three decorators: `simple_logger`, `timer`, and `debug_info`. Each decorator adds specific behavior to the functions they wrap. The `test_function` demonstrates how multiple decorators can be applied to a single function.

### How?

Each decorator is defined as a function that takes another function as an argument. Inside each decorator, a wrapper function is defined that adds the desired behavior and calls the original function.
