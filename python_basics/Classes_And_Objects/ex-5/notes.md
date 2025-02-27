<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Employee Class Example</title>
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

    <h1>Python Employee Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Employee</code> that represents an employee with attributes such as name, employee ID, and position. It includes methods to update the position and display the employee's information.</p>
        
        <h3>Why?</h3>
        <p>Encapsulating employee data and behavior in a class allows for better organization and management of related functionality. This is a key principle of object-oriented programming.</p>
        
        <h3>What?</h3>
        <p>The code creates an instance of the <code>Employee</code> class, updates its position using a defined method, and prints the updated information.</p>
        
        <h3>How?</h3>
        <p>The <code>Employee</code> class has methods to update the position and display the employee's details. An instance of the class is created, its position is updated, and the updated information is displayed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class Employee:
    def __init__(self, name: str, emp_id: int, position: str):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        
    def update_position(self, new_position: str) -> None:
        self.position = new_position
        
    def display_info(self) -> str:
        return f"Employee: {self.name}, ID: {self.emp_id}, Position: {self.position}"

e1 = Employee("Bunny", 777, "DevOps")

print(e1.__dict__)

e1.update_position("backend dev")

print(e1.display_info())
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>