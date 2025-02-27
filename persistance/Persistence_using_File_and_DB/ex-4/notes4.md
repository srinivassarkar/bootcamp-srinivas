<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON Deserialization</title>
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

    <h1>JSON Deserialization</h1>

    <h2>Why Use JSON Deserialization?</h2>
    <p>
        JSON deserialization is the process of recreating a <code>Book</code> object from its 
        JSON representation. This allows you to easily reconstruct objects from data that has 
        been stored or transmitted in JSON format, making it convenient for data exchange 
        between applications.
    </p>

    <h2>What We Will Do</h2>
    <p>
        We will write a class method to create a <code>Book</code> instance from a JSON string, 
        enabling us to easily convert JSON data back into a usable Python object.
    </p>

    <h2>How to Deserialize JSON</h2>
    <p>
        Use the <code>json.loads()</code> function to parse the JSON string and create a 
        <code>Book</code> object.
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

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(**data)

# Example JSON string
book_json = '{"title": "1984", "author": "George Orwell", "year": 1949}'

# Create a Book instance from the JSON string
book_instance = Book.from_json(book_json)
print(book_instance.title)  # Output: 1984
print(book_instance.author)  # Output: George Orwell
print(book_instance.year)    # Output: 1949
    </pre>

    <footer>
        <p>Note: This document was created using Blackbox AI.</p>
    </footer>

</body>
</html>