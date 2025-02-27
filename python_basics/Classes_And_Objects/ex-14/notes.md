# Python Employee Class String Representation

<div class="content">

## Problem Approach

This Python code demonstrates the use of the `__str__` and `__repr__` methods in the `Employee` class to provide string representations of employee objects.

### Why?

The `__str__` method is intended to provide a readable string representation of an object for end-users, while the `__repr__` method is meant for developers and debugging, providing a more detailed representation of the object.

### What?

The `__str__` method returns a simple string that includes the employee's name and position, while the `__repr__` method returns a string that includes all relevant attributes of the employee.

### How?

When you call `repr(emp1)`, it invokes the `__repr__` method, providing a detailed representation of the employee object.
