# Python Employee Class with Properties Example

<div class="content">

## Problem Approach

This Python code defines an `Employee` class that includes properties for managing the position and salary attributes. The class uses private variables and provides validation for setting these attributes.

### Why?

Using properties allows for encapsulation of data, enabling validation and control over how attributes are accessed and modified. This is particularly useful for attributes like position and salary, where you may want to enforce certain rules (e.g., position cannot be empty, salary cannot be negative).

### What?

The `Employee` class has private attributes for position and salary, and properties are defined to get and set these values. If an attempt is made to set an invalid value, a `ValueError` is raised.

### How?

The `position` and `salary` properties are defined using the `@property` decorator for the getter and the `@<property_name>.setter</property_name>` decorator for the setter. This allows for controlled access to the attributes.
