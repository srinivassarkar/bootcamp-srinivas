# Basic Authentication

**Objective:** Implement a login page that requires a username and password.


**Why:** To add a basic layer of security to the Streamlit app by requiring a username and password.

**What:** We use `st.text_input()` to get the username and password, and then validate them against predefined values.

**How:** The app checks if the entered username and password match the predefined values. If they match, the user is granted access; otherwise, an error message is displayed.