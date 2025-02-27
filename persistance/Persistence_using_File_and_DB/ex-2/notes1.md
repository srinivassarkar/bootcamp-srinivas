# Deserialization with Pickle

## Why Use Deserialization?

Deserialization is the process of restoring the serialized object back into memory. This allows you to retrieve the state of an object that was previously saved, enabling you to continue working with it as if it had never been removed from memory.

## What We Will Do

We will read the serialized file and recreate the `Person` object that was saved earlier using Pickle.

## How to Deserialize

Use the `pickle.load()` method to deserialize the object from the file.

## Example Flow

<pre>Save: pickle.dump(p, file) → writes Person object to person.pkl as bytes.
Load: pickle.load(file) → reads bytes from person.pkl, finds Person class in main.py, rebuilds the object.
    </pre>

## Example Code

<pre>import pickle

# Assuming the Person class is already defined as shown previously

# Deserialize the object
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)
    print(loaded_person.name)  # Output: John Doe
    print(loaded_person.educational_institutions)  # Output: ['University A', 'College B']
    print(loaded_person.colleagues)  # Output: ['Alice', 'Bob']
    </pre>

<footer>

Note: This document was created using Blackbox AI.

</footer>