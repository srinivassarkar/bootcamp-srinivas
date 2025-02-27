# Python Class Representations Example

<div class="content">

## Problem Approach

This Python code defines four classes: `Employee`, `Manager`, `Department`, and `Project`. Each class has a custom `__repr__` method that provides a detailed string representation of the object.

### Why?

The `__repr__` method is useful for debugging and logging, as it provides a clear and informative representation of an object, including its attributes.

### What?

The `Employee` class represents an employee, the `Manager` class extends `Employee` with additional information about subordinates, the `Department` class represents a department with its employees, and the `Project` class represents a project associated with a department.

### How?

Each class implements the `__repr__` method to return a string that includes the class name and relevant attributes. This allows for easy inspection of objects when printed.
