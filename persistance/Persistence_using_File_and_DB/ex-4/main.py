import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(**data)

# JSON string
json_string = '{"title": "1984", "author": "George Orwell", "year": 1949}'

# Deserialize from JSON
book = Book.from_json(json_string)
print("Deserialized Book object:")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")






# 4. JSON Deserialization:
#    - Recreated a Book object from its JSON representation.
#    - Used a class method for cleaner object creation.

