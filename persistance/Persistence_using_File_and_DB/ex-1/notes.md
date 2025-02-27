# Basic Serialization with Pickle

## Why Use Pickle?

Pickle is a Python module used for serializing and deserializing Python objects. It’s useful for saving the state of an object to a file and restoring it later. This is particularly helpful in scenarios where you want to save the progress of a program or share data between different Python programs.

## What We Will Do

We’ll create a `Person` class with attributes `name`, `educational_institutions`, and `colleagues`. Then, we’ll serialize an instance of this class to a file using Pickle.

## How to Serialize and Deserialize

Use the `pickle.dump()` method to serialize the object and `pickle.load()` to deserialize it.

## Example Flow

<pre>Save: pickle.dump(p, file) → writes Person object to person.pkl as bytes.
Load: pickle.load(file) → reads bytes from person.pkl, finds Person class in main.py, rebuilds the object.
    </pre>

## Example Code

<pre>import pickle

class Person:
    def __init__(self, name, educational_institutions, colleagues):
        self.name = name
        self.educational_institutions = educational_institutions
        self.colleagues = colleagues

# Create an instance of Person
p = Person("John Doe", ["University A", "College B"], ["Alice", "Bob"])

# Serialize the object
with open('person.pkl', 'wb') as file:
    pickle.dump(p, file)

# Deserialize the object
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)
    print(loaded_person.name)  # Output: John Doe
    </pre>

<footer>

Note: This document was created using Blackbox AI.

</footer>
