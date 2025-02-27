<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Abstract Base Class Example with Animals</title>
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

    <h1>Python Abstract Base Class Example with Animals</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines an abstract base class called <code>Animal</code> using the <code>abc</code> module. The class includes an abstract property <code>sound</code> that must be implemented by any subclass. The <code>Dog</code> and <code>Cat</code> classes inherit from <code>Animal</code> and provide their own implementations of the <code>sound</code> property.</p>
        
        <h3>Why?</h3>
        <p>Abstract base classes are useful for defining a common interface for a group of related classes. They ensure that derived classes implement specific properties or methods, promoting a consistent API and enabling polymorphism.</p>
        
        <h3>What?</h3>
        <p>The <code>Animal</code> class serves as a blueprint for animal types, requiring subclasses to implement the <code>sound</code> property. The <code>Dog</code> and <code>Cat</code> classes provide their own logic for returning the respective sounds.</p>
        
        <h3>How?</h3>
        <p>When instances of <code>Dog</code> and <code>Cat</code> are created, their <code>sound</code> properties can be accessed to retrieve the sounds they make. This demonstrates polymorphism, as the same property name behaves differently depending on the class.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    @property
    def sound(self):
        return "Woof!"

class Cat(Animal):
    @property
    def sound(self):
        return "Meow!"

# Create instances
dog = Dog()
cat = Cat()

print(f"Dog says: {dog.sound}")  # Output: Dog says: Woof!
print(f"Cat says: {cat.sound}")  # Output: Cat says: Meow!
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use abstract base classes in Python to define a common interface for different animal types, allowing for polymorphism and ensuring that all derived classes implement the required properties.
    </div>

</body>
</html>