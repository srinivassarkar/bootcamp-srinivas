# Python Point Class Example with Comparison Methods

<div class="content">

## Problem Approach

This Python code defines a class called `Point` that represents a point in a 2D space with `x` and `y` coordinates. The class includes methods for comparing points based on equality and less-than operations.

### Why?

Implementing comparison methods allows for intuitive comparisons between instances of the class. This is useful for sorting, checking equality, and other operations that rely on comparing objects.

### What?

The `__eq__` method is defined to check if two points are equal by comparing their `x` and `y` coordinates. The `__lt__` method is defined to check if one point is less than another based on both coordinates.

### How?

When instances of the `Point` class are compared using `==` or `<`, the corresponding methods are invoked, allowing for custom comparison logic.
