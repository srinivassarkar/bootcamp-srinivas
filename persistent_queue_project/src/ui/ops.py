# src/ui/ops.py
# Purpose: Streamlit UI for real-time job queue monitoring

import time

import streamlit as st

from src.jobqueue import PersistentQInterface, get_queue

st.set_page_config(page_title="Operations Console", layout="wide")

# Session state for refresh timing
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

st.title("📊 Operations Console")

queue: PersistentQInterface = get_queue()

def auto_refresh() -> None:
    """Trigger page rerun every 5 seconds for live updates."""
    if time.time() - st.session_state.last_refresh >= 5:
        st.session_state.last_refresh = time.time()
        st.rerun()

# Fetch and display job status
status = queue.get_status() or []

st.markdown("### Job Status")
if not status:
    st.warning("No jobs in queue!")
else:
    st.dataframe(status, use_container_width=True)

# Manual refresh option
if st.button("🔄 Refresh Now", key="refresh_now"):
    st.session_state.last_refresh = time.time()
    st.rerun()

st.markdown("---")
st.info("📋 Job details auto-refresh every 5s.")

# Auto-refresh call
auto_refresh()
