# Python Employee and Department Classes Example

<div class="content">

## Problem Approach

This Python code defines two classes: `Employee` and `Department`. The `Employee` class represents an employee with a name and position, while the `Department` class manages a collection of employees.

### Why?

Organizing related data and behavior into classes allows for better structure and management of code, making it easier to maintain and extend.

### What?

The `Department` class can add employees and list them, providing a way to represent a department with its employees.

### How?

The `Department` class initializes its attributes and provides methods to add employees and list them. The `list_employees` method prints the names and positions of employees in the department.

</div>

## Python Code

<pre>class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.name} works as {employee.position} in {self.name}")
    </pre>

<div class="note">**Note:** This code demonstrates the creation of classes in Python to represent employees and their associated department.</div>