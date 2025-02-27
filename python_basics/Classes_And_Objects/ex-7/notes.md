# Python Manager Class Example

<div class="content">

## Problem Approach

This Python code defines a class called `Manager` that represents a manager with attributes such as name, age, and salary. It includes a method to manage a team.

### Why?

Defining a class for a manager allows for encapsulation of related data and behavior, making it easier to manage and interact with manager objects in a program.

### What?

The code creates an instance of the `Manager` class and prints its attributes using the `__dict__` method, which returns the instance's attributes as a dictionary.

### How?

The `Manager` class is defined with an initializer method (`__init__`) that sets the name, age, and salary. An instance of the class is created, and its attributes are printed.

</div>

## Python Code

<pre>class Manager:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def manage(self):
        print(f"{self.name} is managing the team.")

solution = Manager("Bunny", 22, 100000)

print(solution.__dict__)
    </pre>

<div class="note">**Note:** This code demonstrates the creation of a simple class in Python to represent a manager and its attributes.</div>