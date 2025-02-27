# Python Vector Class Example

<div class="content">

## Problem Approach

This Python code defines a class called `Vector` that represents a 2D vector with `x` and `y` components. The class includes methods for vector addition and subtraction, as well as a string representation method.

### Why?

Defining a vector class allows for the encapsulation of vector operations, making it easier to perform arithmetic operations on vectors in a clear and intuitive way.

### What?

The `Vector` class implements the `__add__` and `__sub__` methods to allow for the use of the `+` and `-` operators for vector addition and subtraction, respectively. The `__repr__` method provides a string representation of the vector for easy debugging and display.

### How?

When two `Vector` instances are added or subtracted, the corresponding components are combined, and a new `Vector` instance is returned. The results are printed using the custom string representation defined in the `__repr__` method.


