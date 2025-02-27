# Python Data Persistence Modules

## Query

The modules described in this chapter support storing Python data in a persistent form on disk. The pickle and marshal modules can turn many Python data types into a stream of bytes and then recreate the objects from the bytes. The various DBM-related modules support a family of hash-based file formats that store a mapping of strings to other strings.

## What is this about?

Python modules (pickle, marshal, DBM-related) for saving data to disk and retrieving it later.

## Why do we use it?

To store Python data (objects, strings) persistently outside memory, for reuse or sharing.

## When do we use it?

Use pickle/marshal for serializing complex Python objects (lists, dicts, etc.); use DBM for simple key-value string storage.

## How do we use it?

### Pickle

<pre>import pickle
pickle.dump(data, file)  # Save
data = pickle.load(file)  # Load
    </pre>

### Marshal

<pre>import marshal
marshal.dump(data, file)  # Save
data = marshal.load(file)  # Load (faster but less flexible than pickle)
    </pre>

### DBM

<pre>import dbm
db = dbm.open('file', 'c')  # Create/open DB
db['key'] = 'value'         # Store
db.close()                  # Close
db['key']                    # Retrieve
    </pre>

## Disk Context

"Disk" in this context typically refers to an SSD (Solid-State Drive) or HDD (Hard Disk Drive)—storage devices where Python data can be written to files and stored persistently for later access.

## One Liners

*   **Pickle:** Serializes Python objects into bytes for saving to disk and reloading later.
*   **Marshal:** Fast, internal Python serializer for basic data types, mainly for .pyc files.
*   **DBM:** Stores string key-value pairs in simple, hash-based files on disk.

## Use Cases

*   **Pickle:** Saving a trained machine learning model to disk for later predictions.
*   **Marshal:** Speeding up Python’s compilation by storing bytecode in .pyc files.
*   **DBM:** Storing user preferences as key-value pairs in a small script’s config file.

<footer>

Note: This document was created using Blackbox AI.

</footer>