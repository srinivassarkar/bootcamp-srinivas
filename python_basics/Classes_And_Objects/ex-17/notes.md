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
        <p>This Python code defines a class called <code>Project</code> that represents a project within a department. The class manages a list of employees assigned to the project and provides methods to add, remove, and list employees.</p>
        
        <h3>Why?</h3>
        <p>Managing projects and their associated employees is essential for effective project management. This implementation allows for easy assignment and removal of employees from a project.</p>
        
        <h3>What?</h3>
        <p>The <code>Project</code> class can add and remove employees, list the names of employees working on the project, and provide a string representation that includes the project name, department, and employee names.</p>
        
        <h3>How?</h3>
        <p>The <code>Project</code> class initializes its attributes and provides methods to manage employees. The <code>__str__</code> method returns a string representation of the project, including the department and employee names.</p>
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

class Project:
    def __init__(self, name: str, department: Department) -> None:
        self.name = name
        self.department = department  # Each project belongs to a department
        self.employees: List[Employee] = []  # List of employees working on this project

    def add_employee(self, employee: Employee) -> None:
        """Assigns an employee to the project"""
        self.employees.append(employee)

    def remove_employee(self, emp_id: int) -> None:
        """Removes an employee from the project by ID"""
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self) -> List[str]:
        """Returns a list of employee names in the project"""
        return [emp.name for emp in self.employees]

    def __str__(self) -> str:
        return f"Project: {self.name}, Department: {self.department.name}, Employees: {self.list_employees()}"

# Example Usage
dept = Department("IT")  # Create an IT department

# Create Employees
emp1 = Employee("Alice", 101, "Developer", 60000)
emp2 = Employee("Bob", 102, "Manager", 80000)

# Add employees to the department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Create a project under the IT department
project = Project("Cloud Migration", dept)

# Assign employees to the project
project.add_employee(emp1)
project.add_employee(emp2)

# Display project details
print(project)  # Output: Project: Cloud Migration, Department: IT, Employees: ['Alice', 'Bob']
    </pre>

    <div class=" note">
        <strong>Note:</strong> This code demonstrates the management of projects and their associated employees, allowing for effective tracking of project assignments and modifications.
    </div>

</body>
</html>