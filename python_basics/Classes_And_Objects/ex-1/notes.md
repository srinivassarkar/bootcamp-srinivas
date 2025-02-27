# Python Class Example

<div class="content">

## Problem Approach

This Python code defines a simple class called `Employee` that represents an employee with attributes such as name, employee ID, and position.

### Why?

Classes are a fundamental part of object-oriented programming in Python. They allow you to create objects that encapsulate data and behavior.

### What?

The code creates an instance of the `Employee` class and prints its attributes using the `__dict__` method, which returns the instance's attributes as a dictionary.

### How?

The `Employee` class is defined with an initializer method (`__init__`) that sets the name, employee ID, and position. An instance of the class is created, and its attributes are printed.

</div>

## Python Code

<pre>class Employee:
    def __init__(self, name, emp_id, position): # type: ignore
        self.name = name
        self.emp_id = emp_id
        self.position = position

emp1 = Employee("Bunny", 1, "Developer")

print(emp1.__dict__)
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>
