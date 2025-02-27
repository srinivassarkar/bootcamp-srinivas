<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multipage Streamlit App</title>
</head>
<body>
    <h1>Multipage Streamlit App</h1>
    <p><strong>Objective:</strong> Develop a multipage Streamlit app with navigation.</p>
    <p><strong>Code:</strong></p>
    <pre><code>
# Home.py
import streamlit as st

st.title("Home Page")

# About.py
import streamlit as st

st.title("About Page")
    </code></pre>
    <p><strong>File Structure:</strong></p>
    <pre>
project/
│
├── Home.py
└── About.py
    </pre>
    <p><strong>Why:</strong> To create a multipage app, we need to organize the code into separate files for each page.</p>
    <p><strong>What:</strong> We create two separate Python files, <code>Home.py</code> and <code>About.py</code>, each representing a different page in the app.</p>
    <p><strong>How:</strong> Streamlit automatically detects pages if they are in the same directory. You can navigate between pages using the sidebar.</p>
</body>
</html>