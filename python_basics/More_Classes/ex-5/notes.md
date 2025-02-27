<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Abstract Base Class Example</title>
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

    <h1>Python Abstract Base Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines an abstract base class called <code>Shape</code> using the <code>abc</code> module. The class includes an abstract method <code>area</code> that must be implemented by any subclass. Two subclasses, <code>Circle</code> and <code>Rectangle</code>, provide their own implementations of the <code>area</code> method.</p>
        
        <h3>Why?</h3>
        <p>Abstract base classes are useful for defining a common interface for a group of related classes. They ensure that derived classes implement specific methods, promoting a consistent API and enabling polymorphism.</p>
        
        <h3>What?</h3>
        <p>The <code>Shape</code> class serves as a blueprint for shapes, requiring subclasses to implement the <code>area</code> method. The <code>Circle</code> and <code>Rectangle</code> classes inherit from <code>Shape</code> and provide their own logic for calculating the area.</p>
        
        <h3>How?</h3>
        <p>The <code>Circle</code> class calculates the area using the formula <code>πr²</code>, while the <code>Rectangle</code> class calculates the area using the formula <code>length × width</code>. Instances of both classes are created, and their areas are printed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create instances and calculate area
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use abstract base classes in Python to define a common interface for shapes, allowing for polymorphism and ensuring that all derived classes implement the required methods.
    </div>

</body>
</html>