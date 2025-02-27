# Python Class Method Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `add_method` that adds a new method to a class dynamically. The decorator is applied to the `MyClass` class, allowing instances of this class to call the newly added method.

### Why?

Using decorators to modify classes can be useful for adding functionality without altering the original class definition. This approach promotes code reusability and separation of concerns.

### What?

The `add_method` decorator defines a new method called `new_method` and attaches it to the class it decorates. This method returns a simple string when called.

### How?

When the `MyClass` class is defined, the `add_method` decorator is applied, adding the `new_method` to the class. An instance of `MyClass` is created, and the new method is called to demonstrate its functionality.
