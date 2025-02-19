import streamlit as st

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About"))

# Load the selected page
if page == "Home":
    import home
elif page == "About":
    import about
