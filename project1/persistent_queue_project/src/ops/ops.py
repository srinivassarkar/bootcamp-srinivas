import streamlit as st
from src.queue.sqlite_queue import PersistentQSQLite

st.title("Operations Console")

queue = PersistentQSQLite()
status = queue.get_status()

st.write("### Job Status")
st.table(status)