# Python Abstract Base Class Example with Streaming

<div class="content">

## Problem Approach

This Python code defines an abstract base class called `Streamable` using the `abc` module. The class includes an abstract method `stream` that must be implemented by any subclass. The `VideoStream` and `AudioStream` classes inherit from `Streamable` and provide their own implementations of the `stream` method.

### Why?

Abstract base classes are useful for defining a common interface for a group of related classes. They ensure that derived classes implement specific methods, promoting a consistent API and enabling polymorphism.

### What?

The `Streamable` class serves as a blueprint for streamable content, requiring subclasses to implement the `stream` method. The `VideoStream` and `AudioStream` classes provide their own logic for streaming video and audio, respectively.

### How?

When instances of `VideoStream` and `AudioStream` are created, their `stream` methods can be called to retrieve the respective streaming messages. This demonstrates polymorphism, as the same method name behaves differently depending on the class.
