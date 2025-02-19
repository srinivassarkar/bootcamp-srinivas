
import streamlit as st

st.title("Slider App")

value = st.slider("Select a value", 0, 100, 50)
st.write(f"Selected value: {value}")
