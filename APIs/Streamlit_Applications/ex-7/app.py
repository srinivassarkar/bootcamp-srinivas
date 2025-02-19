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
