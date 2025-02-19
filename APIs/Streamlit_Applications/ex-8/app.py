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
