# Python Temperature Class Example

<div class="content">

## Problem Approach

This Python code defines a class called `Temperature` that represents a temperature in Celsius. The class uses a property to manage the temperature value, ensuring that it stays within a valid range.

### Why?

Using properties allows for encapsulation of data and validation logic. This ensures that any temperature value assigned to the instance is checked for validity, preventing invalid states.

### What?

The `celsius` property provides a way to get and set the temperature value. The setter method includes validation to ensure that the temperature is within the range of -273.15°C (absolute zero) to 5000°C.

### How?

When an instance of the `Temperature` class is created, the initial temperature is set using the setter. If an invalid temperature is assigned later, a `ValueError` is raised, which can be caught and handled appropriately.

</div>
