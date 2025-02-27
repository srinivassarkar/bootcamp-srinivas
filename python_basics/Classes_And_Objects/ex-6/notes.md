<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Employee and Manager Classes Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-x: auto;
        }
        .content {
            margin-bottom: 20px;
        }
        .note {
            background-color: #e7f3fe;
            border-left: 6px solid #2196F3;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Python Employee and Manager Classes Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Employee</code> and a subclass called <code>Manager</code>. The <code>Manager</code> class inherits from <code>Employee</code> and adds functionality to manage subordinates.</p>
        
        <h3>Why?</h3>
        <p>Using inheritance allows for code reuse and the creation of a hierarchical relationship between classes. This is a fundamental concept in object-oriented programming.</p>
        
        <h3>What?</h3>
        <p>The code creates a manager and two employees, adds the employees as subordinates to the manager, and prints the manager's information, including the number of subordinates managed.</p>
        
        <h3>How?</h3>
        <p>The <code>Employee</code> class has a <code>__str__</code> method for string representation. The <code>Manager</code> class overrides this method to include the count of subordinates. Instances of both classes are created, and the manager's details are printed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

class Manager(Employee):
    def __init__(self, name, salary, position):
        super().__init__(name, salary, position)
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def __str__(self):
        return f"{super().__str__()} manages {len(self.subordinates)} employees"

manager = Manager("Alice", 80000, "Senior Manager")
emp1 = Employee("Bob", 50000, "Developer")
emp2 = Employee("Charlie", 60000, "Designer")
manager.add_subordinate(emp1)
manager.add_subordinate(emp2)
print(manager)
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using deep seek to solve and understand the concepts of inheritance and string representation in Python.
    </div>

</body>
</html>