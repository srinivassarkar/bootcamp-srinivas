# Python Class with Type Annotations Example

<div class="content">

## Problem Approach

This Python code defines a class called `Employee` that represents an employee with attributes such as name, employee ID, and position, using type annotations for better clarity and type checking.

### Why?

Type annotations help improve code readability and enable static type checking, which can catch errors before runtime. This is especially useful in larger codebases.

### What?

The code creates an instance of the `Employee` class and prints its attributes using the `__dict__` method, which returns the instance's attributes as a dictionary.

### How?

The `Employee` class is defined with an initializer method (`__init__`) that sets the name, employee ID, and position with type annotations. An instance of the class is created, and its attributes are printed.

</div>

## Python Code

<pre>class Employee:
    def __init__(self, name: str, emp_id: int, position: str):
        self.name: str = name
        self.emp_id: int = emp_id
        self.position: str = position

emp1 = Employee("Bunny", 1, "Developer")

print(emp1.__dict__)
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>