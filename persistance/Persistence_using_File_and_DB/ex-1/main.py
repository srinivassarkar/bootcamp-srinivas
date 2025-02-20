import pickle

class Person:
    def __init__(self, name: str, educational_institutions: str, colleagues: str):
        self.name = name
        self.educational_institutions = educational_institutions
        self.colleagues = colleagues

# Create an instance of Person
person = Person("Alice", ["Harvard", "MIT"], ["Bob", "Charlie"])

# Serialize to a file
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)

print("Person object serialized to person.pkl")

# 1. Basic Serialization with Pickle:
#    - Used Pickle to serialize a Person object to a file.
#    - Pickle is ideal for Python-specific serialization.
