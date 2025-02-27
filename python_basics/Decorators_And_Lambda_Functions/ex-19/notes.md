# Python Total Ordering Example

<div class="content">

## Problem Approach

This Python code defines a class called `Point` that represents a point in a 2D space. The class uses the `functools.total_ordering` decorator to automatically generate the rich comparison methods based on the defined `__lt__` (less than) and `__eq__` (equal to) methods.

### Why?

Implementing all comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__`, and `__ne__`) can be tedious and error-prone. The `total_ordering` decorator simplifies this by allowing you to define only the necessary methods, while it automatically provides the rest.

### What?

The `Point` class defines the `__lt__` method to compare points based on their distance from the origin (calculated as the square root of the sum of the squares of their coordinates) and the `__eq__` method to check for equality based on their coordinates.

### How?

The `total_ordering` decorator is applied to the `Point` class, which requires the implementation of at least one less-than method and one equality method. The decorator then generates the other comparison methods automatically.

</div>

## Python Code

<pre>from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

# Example Usage
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 < p2)  # Output: True
    </pre>

<div class="note">**Note:** This code demonstrates how to use the `total_ordering` decorator in Python to simplify the implementation of comparison methods in a class, making it easier to work with custom objects in sorting and comparisons.</div>