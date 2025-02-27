<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Project Class Example</title>
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

    <h1>Python Project Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Project</code> that represents a project within a department. The class manages a list of employees assigned to the project.</p>
        
        <h3>Why?</h3>
        <p>Managing projects and their associated employees is essential for effective project management. This implementation allows for easy addition of employees to a project.</p>
        
        <h3>What?</h3>
        <p>The <code>Project</code> class can add employees and provide a string representation that includes the project name and the names of employees assigned to it.</p>
        
        <h3>How?</h3>
        <p>The <code>Project</code> class initializes its attributes and provides methods to add employees. The <code>__str__</code> method returns a string representation of the project and its employees.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from typing import List

class Employee:
    def __init__(self, name: str, salary: float, position: str) -> None:
        self.name = name
        self.salary = salary
        self.position = position

    def __str__(self) -> str:
        return f"{self.name} ({self.position})"

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def __str__(self) -> str:
        return f"Department: {self.name}, Employees: {[str(emp) for emp in self.employees]}"

class Project:
    def __init__(self, name: str, department: Department) -> None:
        self.name = name
        self.department = department
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def __str__(self) -> str:
        return f"Project: {self.name}, Employees: {[emp.name for emp in self.employees]}"

# Example Usage
dept = Department("IT")
emp1 = Employee("Alice", 60000, "Developer")
dept.add_employee(emp1)

project = Project("Cloud Migration", dept)
project.add_employee(emp1)
print(project)  # Output: Project: Cloud Migration, Employees: ['Alice']
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates the management of projects and their associated employees, allowing for effective tracking of project assignments.
    </div>

</body>
</html>