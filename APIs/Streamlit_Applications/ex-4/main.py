
import streamlit as st

USERNAME = "admin"
PASSWORD = "password"

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Logged in successfully!")
        st.write("Welcome to the main app content.")
    else:
        st.error("Invalid username or password")
