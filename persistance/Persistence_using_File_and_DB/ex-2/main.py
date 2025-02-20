import pickle

# Define the Person class with the expected attributes
class Person:
    def __init__(self, name, educational_institutions, colleagues):
        self.name = name
        self.educational_institutions = educational_institutions
        self.colleagues = colleagues

# Deserialize from the file
with open("person.pkl", "rb") as file:
    person = pickle.load(file)

print("Deserialized Person object:")
print(f"Name: {person.name}")
print(f"Education: {person.educational_institutions}")
print(f"Colleagues: {person.colleagues}")


# 2. Deserialization with Pickle:
#    - Restored the Person object from the serialized file.
#    - Pickle handles the conversion back to a Python object.