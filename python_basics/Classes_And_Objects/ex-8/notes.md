<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python SuperManager Class Example</title>
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

    <h1>Python SuperManager Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>SuperManager</code> that inherits from the <code>Manager</code> class. The <code>SuperManager</code> class adds functionality to manage subordinates.</p>
        
        <h3>Why?</h3>
        <p>Using inheritance allows for code reuse and the creation of a hierarchical relationship between classes. This is a fundamental concept in object-oriented programming.</p>
        
        <h3>What?</h3>
        <p>The <code>SuperManager</code> class can add subordinates and manage them, providing a way to represent a manager who oversees other managers or employees.</p>
        
        <h3>How?</h3>
        <p>The <code>SuperManager</code> class initializes its attributes using the parent class's constructor and adds methods to add subordinates and manage them. The <code>manage_subordinates</code> method prints the names of the subordinates being managed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class SuperManager(Manager):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def manage_subordinates(self):
        for subordinate in self.subordinates:
            print(f"{self.name} is managing {subordinate.name}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates the use of inheritance in Python to create a specialized manager class that can manage other employees.
    </div>

</body>
</html>