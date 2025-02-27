# Python Abstract Base Class Example

<div class="content">

## Problem Approach

This Python code defines an abstract base class called `Shape` using the `abc` module. The class includes an abstract method `area` that must be implemented by any subclass. Two subclasses, `Circle` and `Rectangle`, provide their own implementations of the `area` method.

### Why?

Abstract base classes are useful for defining a common interface for a group of related classes. They ensure that derived classes implement specific methods, promoting a consistent API and enabling polymorphism.

### What?

The `Shape` class serves as a blueprint for shapes, requiring subclasses to implement the `area` method. The `Circle` and `Rectangle` classes inherit from `Shape` and provide their own logic for calculating the area.

### How?

The `Circle` class calculates the area using the formula `πr²`, while the `Rectangle` class calculates the area using the formula `length × width`. Instances of both classes are created, and their areas are printed.
