<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Vector Class Example</title>
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

    <h1>Python Vector Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Vector</code> that represents a 2D vector with <code>x</code> and <code>y</code> components. The class includes methods for vector addition and subtraction, as well as a string representation method.</p>
        
        <h3>Why?</h3>
        <p>Defining a vector class allows for the encapsulation of vector operations, making it easier to perform arithmetic operations on vectors in a clear and intuitive way.</p>
        
        <h3>What?</h3>
        <p>The <code>Vector</code> class implements the <code>__add__</code> and <code>__sub__</code> methods to allow for the use of the <code>+</code> and <code>-</code> operators for vector addition and subtraction, respectively. The <code>__repr__</code> method provides a string representation of the vector for easy debugging and display.</p>
        
        <h3>How?</h3>
        <p>When two <code>Vector</code> instances are added or subtracted, the corresponding components are combined, and a new <code>Vector</code> instance is returned. The results are printed using the custom string representation defined in the <code>__repr__</code> method.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Create instances and perform arithmetic
v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(f"Addition: {v1 + v2}")  # Output: Vector(3, 7)
print(f"Subtraction: {v1 - v2}")  # Output: Vector(1, -1)
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to implement a simple vector class in Python, allowing for intuitive arithmetic operations and providing a clear representation of vector instances.
    </div>

</body>
</html>