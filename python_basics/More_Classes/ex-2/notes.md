<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Book Class with ISBN Validation Example</title>
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

    <h1>Python Book Class with ISBN Validation Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Book</code> that represents a book with a title and an author. The class includes a static method <code>validate_isbn</code> that checks if a given ISBN is valid based on its length and whether it consists only of digits.</p>
        
        <h3>Why?</h3>
        <p>Static methods are useful for utility functions that are related to the class but do not require access to instance-specific data. In this case, validating an ISBN does not depend on the attributes of a specific book instance.</p>
        
        <h3>What?</h3>
        <p>The <code>validate_isbn</code> method checks if the provided ISBN is either 10 or 13 characters long and consists only of digits. This is a basic validation for ISBNs.</p>
        
        <h3>How?</h3>
        <p>The static method is defined using the <code>@staticmethod</code> decorator, allowing it to be called on the class itself without needing an instance. The method can be called directly using the class name.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) in [10, 13] and isbn.isdigit()

# Example Usage
isbn = "1234567890"
print(f"Is {isbn} a valid ISBN? {Book.validate_isbn(isbn)}")  # Output: True
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to define a static method in a Python class for validating ISBN numbers, allowing for utility functions that are related to the class but do not require instance data.
    </div>

</body>
</html>