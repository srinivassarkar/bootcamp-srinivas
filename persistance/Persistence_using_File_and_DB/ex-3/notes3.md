<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Serialization with JSON</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-left: 5px solid #3498db;
            overflow-x: auto;
        }
        footer {
            margin-top: 20px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>

    <h1>Serialization with JSON</h1>

    <h2>Why Use JSON?</h2>
    <p>
        JSON (JavaScript Object Notation) is a lightweight data interchange format that’s 
        human-readable and widely used. It is easy to read and write for humans and easy to 
        parse and generate for machines, making it a popular choice for data exchange between 
        web services and applications.
    </p>

    <h2>What We Will Do</h2>
    <p>
        We will convert a <code>Book</code> object to a JSON string, allowing us to easily 
        store and transmit the book's data in a standardized format.
    </p>

    <h2>How to Convert to JSON</h2>
    <p>
        Implement a <code>to_json()</code> method in the <code>Book</code> class using the 
        <code>json</code> module to serialize the object.
    </p>

    <h2>Example Code</h2>
    <pre>
import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_json(self):
        return json.dumps(self.__dict__)

# Create an instance of Book
book = Book("1984", "George Orwell", 1949)

# Convert the Book object to a JSON string
book_json = book.to_json()
print(book_json)  # Output: {"title": "1984", "author": "George Orwell", "year": 1949}
    </pre>

    <footer>
        <p>Note: This document was created using Blackbox AI.</p>
    </footer>

</body>
</html>