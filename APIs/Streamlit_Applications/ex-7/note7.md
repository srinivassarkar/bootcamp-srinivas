<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Data Tables with Pandas</title>
</head>
<body>
    <h1>Interactive Data Tables with Pandas</h1>
    <p><strong>Objective:</strong> Load a dataset into a Pandas DataFrame and display it interactively.</p>
    <p><strong>Code:</strong></p>
    <pre><code>
# app.py
import streamlit as st
import pandas as pd

st.title("Interactive Data Table")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
st.dataframe(df)
    </code></pre>
    <p><strong>File Structure:</strong></p>
    <pre>
project/
│
└── app.py
    </pre>
    <p><strong>Why:</strong> To demonstrate how to display and interact with data tables in Streamlit.</p>
    <p><strong>What:</strong> We create a Pandas DataFrame and use <code>st.dataframe()</code> to display it.</p>
    <p><strong>How:</strong> The <code>st.dataframe()</code> function renders the DataFrame as an interactive table in the Streamlit app.</p>
</body>
</html>