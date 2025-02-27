# Python Abstract Base Class Example with Animals

<div class="content">

## Problem Approach

This Python code defines an abstract base class called `Animal` using the `abc` module. The class includes an abstract property `sound` that must be implemented by any subclass. The `Dog` and `Cat` classes inherit from `Animal` and provide their own implementations of the `sound` property.

### Why?

Abstract base classes are useful for defining a common interface for a group of related classes. They ensure that derived classes implement specific properties or methods, promoting a consistent API and enabling polymorphism.

### What?

The `Animal` class serves as a blueprint for animal types, requiring subclasses to implement the `sound` property. The `Dog` and `Cat` classes provide their own logic for returning the respective sounds.

### How?

When instances of `Dog` and `Cat` are created, their `sound` properties can be accessed to retrieve the sounds they make. This demonstrates polymorphism, as the same property name behaves differently depending on the class.
