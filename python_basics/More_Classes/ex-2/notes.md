# Python Book Class with ISBN Validation Example

<div class="content">

## Problem Approach

This Python code defines a class called `Book` that represents a book with a title and an author. The class includes a static method `validate_isbn` that checks if a given ISBN is valid based on its length and whether it consists only of digits.

### Why?

Static methods are useful for utility functions that are related to the class but do not require access to instance-specific data. In this case, validating an ISBN does not depend on the attributes of a specific book instance.

### What?

The `validate_isbn` method checks if the provided ISBN is either 10 or 13 characters long and consists only of digits. This is a basic validation for ISBNs.

### How?

The static method is defined using the `@staticmethod` decorator, allowing it to be called on the class itself without needing an instance. The method can be called directly using the class name.

</div>

## Python Code

<pre>class Book:
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

<div class="note">**Note:** This code demonstrates how to define a static method in a Python class for validating ISBN numbers, allowing for utility functions that are related to the class but do not require instance data.</div>