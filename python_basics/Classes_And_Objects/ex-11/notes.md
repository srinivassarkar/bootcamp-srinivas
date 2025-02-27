<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Employee and Department Classes Example</title>
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

    <h1>Python Employee and Department Classes Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines two classes: <code>Employee</code> and <code>Department</code>. The <code>Employee</code> class represents an employee with attributes such as name, employee ID, position, and salary. The <code>Department</code> class manages a collection of employees.</p>
        
        <h3>Why?</h3>
        <p>Using classes allows for better organization of related data and behavior, making it easier to manage and extend the code.</p>
        
        <h3>What?</h3>
        <p>The <code>Department</code> class can add employees and provide a string representation that includes the department name and its employees.</p>
        
        <h3>How?</h3>
        <p>The <code>Employee</code> class has a <code>__str__</code> method for string representation. The <code>Department</code> class initializes its attributes and provides methods to add employees and represent the department as a string. Instances of both classes are created, and the department's details are printed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from typing import List

class Employee:
    def __init__(self, name: str, emp_id: int, position: str, salary: float) -> None:
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary

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

emp1 = Employee("Alice", 101, "Developer", 60000)
emp2 = Employee("Bob", 102, "Manager", 80000)

dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

print(dept)
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates the creation of classes in Python to represent employees and their associated department, including type annotations for better clarity.
    </div>

</body>
</html>