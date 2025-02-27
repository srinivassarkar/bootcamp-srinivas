# Python Employee Class with Property Example

<div class="content">

## Problem Approach

This Python code defines an `Employee` class that includes a property for managing the salary attribute. The salary is stored privately and can be accessed and modified through a property.

### Why?

Using properties allows for encapsulation of data, enabling validation and control over how attributes are accessed and modified. This is particularly useful for attributes like salary, where you may want to enforce certain rules (e.g., salary must be positive).

### What?

The `Employee` class has a private attribute for salary, and a property is defined to get and set the salary value. If an attempt is made to set a negative salary, a `ValueError` is raised.

### How?

The `salary` property is defined using the `@property` decorator for the getter and the `@salary.setter` decorator for the setter. This allows for controlled access to the salary attribute.
