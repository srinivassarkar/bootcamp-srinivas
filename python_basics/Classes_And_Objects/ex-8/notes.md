# Python SuperManager Class Example

<div class="content">

## Problem Approach

This Python code defines a class called `SuperManager` that inherits from the `Manager` class. The `SuperManager` class adds functionality to manage subordinates.

### Why?

Using inheritance allows for code reuse and the creation of a hierarchical relationship between classes. This is a fundamental concept in object-oriented programming.

### What?

The `SuperManager` class can add subordinates and manage them, providing a way to represent a manager who oversees other managers or employees.

### How?

The `SuperManager` class initializes its attributes using the parent class's constructor and adds methods to add subordinates and manage them. The `manage_subordinates` method prints the names of the subordinates being managed.

</div>

## Python Code

<pre>class SuperManager(Manager):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def manage_subordinates(self):
        for subordinate in self.subordinates:
            print(f"{self.name} is managing {subordinate.name}")
    </pre>

<div class="note">**Note:** This code demonstrates the use of inheritance in Python to create a specialized manager class that can manage other employees.</div>