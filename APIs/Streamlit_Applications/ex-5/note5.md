<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reactivity Using Widgets</title>
</head>
<body>
    <h1>Reactivity Using Widgets</h1>
    <p><strong>Objective:</strong> Create an app with a slider widget that dynamically updates a displayed number.</p>
    <p><strong>Code:</strong></p>
    <pre><code>
# app.py
import streamlit as st

st.title("Slider App")

value = st.slider("Select a value", 0, 100, 50)
st.write(f"Selected value: {value}")
    </code></pre>
    <p><strong>File Structure:</strong></p>
    <pre>
project/
│
└── app.py
    </pre>
    <p><strong>Why:</strong> To demonstrate how Streamlit's widgets can be used to create reactive apps.</p>
    <p><strong>What:</strong> We use <code>st.slider()</code> to create a slider widget that allows the user to select a value.</p>
    <p><strong>How:</strong> The <code>st.slider()</code> function creates a slider that the user can interact with. The selected value is displayed in real-time using <code>st.write()</code>.</p>
</body>
</html>