
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

# Serialize to JSON
json_string = book.to_json()
print("JSON representation of Book:")
print(json_string)





# 3. JSON Serialization:
#    - Converted a Book object to a JSON string.
#    - JSON is human-readable and widely used for APIs.

