<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Department Class with Salary Management</title>
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

    <h1>Python Department Class with Salary Management</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Department</code> that manages employees. It includes methods to add and remove employees, as well as to calculate the total salary of all employees in the department.</p>
        
        <h3>Why?</h3>
        <p>Managing employee data efficiently is crucial for organizations. This implementation allows for easy addition, removal, and salary calculations for employees within a department.</p>
        
        <h3>What?</h3>
        <p>The <code>Department</code> class can add employees, remove them, and calculate the total salary of all employees. It also provides a string representation of the department and its employees.</p>
        
        <h3>How?</h3>
        <p>The <code>Department</code> class initializes its attributes and provides methods to manage employees. The <code>calculate_total_salary</code> method sums the salaries of all employees, and the <code>remove_employee</code> method allows for the removal of an employee by their ID.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from typing import Dict

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
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        self.employees[employee.emp_id] = employee

    def remove_employee(self, emp_id: int) -> None:
        if emp_id in self.employees:
            del self.employees[emp_id]

    def calculate_total_salary(self) -> float:
        return sum(emp.salary for emp in self.employees.values())

    def __str__(self) -> str:
        return f"Department: {self.name}, Employees: {list(self.employees.values())}"

# Example Usage
dept = Department("IT")
dept.add_employee(Employee("Alice", 101, "Developer", 60000))
dept.add_employee(Employee("Bob", 102, "Manager", 80000))

print(f"Total Department Salary: {dept.calculate_total_salary()}")  # 140000
dept.remove_employee(102)
print(dept)  # Bob removed
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates the management of employee data within a department, including salary calculations and employee removal.
    </div>

</body>
</html>