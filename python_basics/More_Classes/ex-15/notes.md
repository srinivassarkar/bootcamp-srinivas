# Python Point Class with Properties Example

<div class="content">

## Problem Approach

This Python code defines a class called `Point` that represents a point in a 2D space with `x` and `y` coordinates. The class uses properties to provide read-only access to these coordinates.

### Why?

Using properties allows for encapsulation of data, providing controlled access to class attributes. In this case, the coordinates are made read-only to prevent modification after the object is created.

### What?

The `x` and `y` properties provide access to the private attributes `_x` and `_y`. The `__repr__` method is defined to provide a string representation of the point for easy debugging and display.

### How?

When an instance of the `Point` class is created, the coordinates are set through the constructor. The properties allow for reading the values, but attempting to set them raises an `AttributeError`, demonstrating their read-only nature.
