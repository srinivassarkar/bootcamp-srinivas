# Python Class Instance Counter Example

<div class="content">

## Problem Approach

This Python code defines a class called `MyClass` that includes a static variable `num_instances` to keep track of the total number of instances created. The class also includes a static method to retrieve this count.

### Why?

Using a static variable allows the class to maintain a count of instances across all instances. This is useful for tracking how many objects of a class have been created without needing to store this information in each instance.

### What?

The `num_instances` variable is incremented each time a new instance of `MyClass` is created. The static method `get_num_instances` returns the current count of instances.

### How?

The static method is defined using the `@staticmethod` decorator, which allows it to be called on the class itself without needing an instance. It accesses the class variable directly to return the count of instances.
