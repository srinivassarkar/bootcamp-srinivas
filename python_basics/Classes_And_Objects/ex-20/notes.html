<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Company Class Example</title>
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

    <h1>Python Company Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Company</code> that manages departments, projects, and employees. The class provides methods to add departments and projects, assign employees to projects, and print summaries of departments and projects.</p>
        
        <h3>Why?</h3>
        <p>Managing a company structure with departments and projects allows for better organization and tracking of employees and their assignments. This implementation provides a clear way to manage these relationships.</p>
        
        <h3>What?</h3>
        <p>The <code>Company</code> class can add departments and projects, assign employees to specific projects, and provide summaries of departments and projects, including their employees.</p>
        
        <h3>How?</h3>
        <p>The <code>Company</code> class initializes its attributes and provides methods to manage departments and projects. It also includes methods to print summaries of the company's structure.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from typing import List

class Employee:
    def __init__(self, name: str, emp_id: int, position: str, salary: float) -> None:
        self.name = name
        self.emp_id = emp_id
        self._position = position
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Salary must be positive!")
        self._salary = value

    def __str__(self) -> str:
        return f"Employee: {self.name}, ID: {self.emp_id}, Position: {self._position}, Salary: ${self.salary}"

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def list_employees(self) -> List[str]:
        return [emp.name for emp in self.employees]

    def __str__(self) -> str:
        return f"Department: {self.name}, Employees: {self.list_employees()}"

class Project:
    def __init__(self, name: str, department: Department) -> None:
        self.name = name
        self.department = department
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def __str__(self) -> str:
        return f"Project: {self.name}, Department: {self.department.name}, Employees: {[emp.name for emp in self.employees]}"

class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: List[Department] = []
        self.projects: List[Project] = []

    def add_department(self, department: Department) -> None:
        """Adds a new department to the company"""
        self.departments.append(department)

    def add_project(self, project: Project) -> None:
        """Adds a new project to the company"""
        self.projects.append(project)

    def assign_employee_to_project(self, emp: Employee, project_name: str) -> None:
        """Assigns an employee to a project by name"""
        for project in self.projects:
            if project.name == project_name:
                project.add_employee(emp)
                return
        raise ValueError(f"Project '{project_name}' not found!")

    def department_summary(self) -> None:
        """Prints a summary of all departments and their employees"""
        print(f"\nCompany: {self.name} - Departments Summary")
        for dept in self.departments:
            print(f"\n{dept}")

    def project_summary(self) -> None:
        """Prints a summary of all projects and their assigned employees"""
        print(f"\nCompany: {self.name