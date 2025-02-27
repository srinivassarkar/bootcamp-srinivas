# Python Class with Multiple Instances Example

<div class="content">

## Problem Approach

This Python code defines a class called `Employee` that represents an employee with attributes such as name, employee ID, and position. It creates multiple instances of the class and prints their attributes.

### Why?

Creating multiple instances of a class allows you to represent different objects with the same structure. This is a fundamental concept in object-oriented programming.

### What?

The code creates two instances of the `Employee` class and prints their attributes using the `__dict__` method, which returns the instance's attributes as a dictionary.

### How?

The `Employee` class is defined with an initializer method (`__init__`) that sets the name, employee ID, and position with type annotations. Two instances of the class are created, and their attributes are printed.

</div>

## Python Code

<pre>class Employee:
    def __init__(self, name: str, emp_id: int, position: str) -> None:
        self.name: str = name
        self.emp_id: int = emp_id
        self.position: str = position

e1 = Employee("Ashkok", 101, "Developer")
e2 = Employee("Naresh", 102, "Tester")
print(e1.__dict__)
print(e2.__dict__)
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>