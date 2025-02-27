# State Management with Session State

**Objective:** Build a counter app that increments a number each time a button is pressed.



**Why:** To demonstrate how to manage state in a Streamlit app using `st.session_state`.

**What:** We use `st.session_state` to store and update the count value across button clicks.

**How:** The `st.session_state` object is used to persist the state across reruns. When the button is clicked, the count is incremented and displayed.