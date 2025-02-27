<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Data Persistence Modules</title>
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

    <h1>Python Data Persistence Modules</h1>

    <h2>Query</h2>
    <p>
        The modules described in this chapter support storing Python data in a persistent form on disk. 
        The pickle and marshal modules can turn many Python data types into a stream of bytes and then 
        recreate the objects from the bytes. The various DBM-related modules support a family of 
        hash-based file formats that store a mapping of strings to other strings.
    </p>

    <h2>What is this about?</h2>
    <p>
        Python modules (pickle, marshal, DBM-related) for saving data to disk and retrieving it later.
    </p>

    <h2>Why do we use it?</h2>
    <p>
        To store Python data (objects, strings) persistently outside memory, for reuse or sharing.
    </p>

    <h2>When do we use it?</h2>
    <p>
        Use pickle/marshal for serializing complex Python objects (lists, dicts, etc.); use DBM for 
        simple key-value string storage.
    </p>

    <h2>How do we use it?</h2>
    <h3>Pickle</h3>
    <pre>
import pickle
pickle.dump(data, file)  # Save
data = pickle.load(file)  # Load
    </pre>

    <h3>Marshal</h3>
    <pre>
import marshal
marshal.dump(data, file)  # Save
data = marshal.load(file)  # Load (faster but less flexible than pickle)
    </pre>

    <h3>DBM</h3>
    <pre>
import dbm
db = dbm.open('file', 'c')  # Create/open DB
db['key'] = 'value'         # Store
db.close()                  # Close
db['key']                    # Retrieve
    </pre>

    <h2>Disk Context</h2>
    <p>
        "Disk" in this context typically refers to an SSD (Solid-State Drive) or HDD (Hard Disk Drive)—storage 
        devices where Python data can be written to files and stored persistently for later access.
    </p>

    <h2>One Liners</h2>
    <ul>
        <li><strong>Pickle:</strong> Serializes Python objects into bytes for saving to disk and reloading later.</li>
        <li><strong>Marshal:</strong> Fast, internal Python serializer for basic data types, mainly for .pyc files.</li>
        <li><strong>DBM:</strong> Stores string key-value pairs in simple, hash-based files on disk.</li>
    </ul>

    <h2>Use Cases</h2>
    <ul>
        <li><strong>Pickle:</strong> Saving a trained machine learning model to disk for later predictions.</li>
        <li><strong>Marshal:</strong> Speeding up Python’s compilation by storing bytecode in .pyc files.</li>
        <li><strong>DBM:</strong> Storing user preferences as key-value pairs in a small script’s config file.</li>
    </ul>

    <footer>
        <p>Note: This document was created using Blackbox AI.</p>
    </footer>

</body>
</html>