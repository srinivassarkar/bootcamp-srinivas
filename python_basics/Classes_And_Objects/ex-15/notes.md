<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Class Representations Example</title>
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

    <h1>Python Class Representations Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines four classes: <code>Employee</code>, <code>Manager</code>, <code>Department</code>, and <code>Project</code>. Each class has a custom <code>__repr__</code> method that provides a detailed string representation of the object.</p>
        
        <h3>Why?</h3>
        <p>The <code>__repr__</code> method is useful for debugging and logging, as it provides a clear and informative representation of an object, including its attributes.</p>
        
        <h3>What?</h3>
        <p>The <code>Employee</code> class represents an employee, the <code>Manager</code> class extends <code>Employee</code> with additional information about subordinates, the <code>Department</code> class represents a department with its employees, and the <code>Project</code> class represents a project associated with a department.</p>
        
        <h3>How?</h3>
        <p>Each class implements the <code>__repr__</code> method to return a string that includes the class name and relevant attributes. This allows for easy inspection of objects when printed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class Employee:
    def __init__(self, name: str, salary: float, position: str) -> None:
        self.name = name
        self.salary = salary
        self.position = position

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary}, position={self.position})"

class Manager(Employee):
    def __init__(self, name: str, salary: float, position: str) -> None:
        super().__init__(name, salary, position)
        self.subordinates = []

    def __repr__(self):
        return f"Manager(name={self.name}, salary={self.salary}, position={self.position}, subordinates={len(self.subordinates)})"

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def __repr__(self):
        return f"Department(name={self.name}, employees={len(self.employees)})"

class Project:
    def __init__(self, name: str, department: Department) -> None:
        self.name = name
        self.department = department
        self.employees = []

    def __repr__(self):
        return f"Project(name={self.name}, department={self.department.name}, employees={len(self.employees)})"

# Test
emp1 = Employee("Alice", 60000, "Developer")
manager = Manager("Bob", 80000, "Manager")
dept = Department("IT")
project = Project("Project A", dept)

print(repr(emp1))
print(repr(manager))
print(repr(dept))
print(repr(project))
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates the use of the <code>__repr__</code> method in Python classes to provide detailed representations of objects for debugging and logging purposes.
    </div>

</body>
</html>