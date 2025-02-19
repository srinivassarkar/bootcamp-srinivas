
import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

st.title("Counter App")

if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")
