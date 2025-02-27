<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plotly for Advanced Graphs</title>
</head>
<body>
    <h1>Plotly for Advanced Graphs</h1>
    <p><strong>Objective:</strong> Embed a Plotly scatter plot in a Streamlit app.</p>
    <p><strong>Code:</strong></p>
    <pre><code>
# app.py
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Plotly Scatter Plot")

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})

fig = px.scatter(df, x='x', y='y')
st.plotly_chart(fig)
    </code></pre>
    <p><strong>File Structure:</strong></p>
    <pre>
project/
│
└── app.py
    </pre>
    <p><strong>Why:</strong> To demonstrate how to create and display advanced interactive graphs using Plotly in Streamlit.</p>
    <p><strong>What:</strong> We use Plotly Express to create a scatter plot and then display it using <code>st.plotly_chart()</code>.</p>
    <p><strong>How:</strong> The <code>st.plotly_chart()</code> function is used to render the Plotly figure in the Streamlit app.</p>
</body>
</html>