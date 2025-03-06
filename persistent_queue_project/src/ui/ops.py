# src/ui/ops.py
"""Streamlit UI for real-time job queue monitoring."""

import time
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st

from src.jobqueue import PersistentQInterface, get_queue

st.set_page_config(page_title="Operations Console", layout="wide")

if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

st.title("📊 Operations Console")

queue: PersistentQInterface = get_queue()

def auto_refresh() -> None:
    """Trigger page rerun every 5 seconds."""
    if time.time() - st.session_state.last_refresh >= 5:
        st.session_state.last_refresh = time.time()
        st.rerun()

status = queue.get_status() or []
df = pd.DataFrame(status)
stale_jobs = df[(df["status"] == "PROCESSING") &
                (df["last_heartbeat"] < (datetime.now() - timedelta(minutes=5)).isoformat())]
if not stale_jobs.empty:
    st.warning(f"Detected {len(stale_jobs)} stalled jobs—check Manager UI!")

st.markdown("### Job Status")
if not status:
    st.warning("No jobs in queue!")
else:
    st.dataframe(df, use_container_width=True)

if st.button("🔄 Refresh Now", key="refresh_now"):
    st.session_state.last_refresh = time.time()
    st.rerun()

st.markdown("---")
st.info("📋 Job details auto-refresh every 5s.")

auto_refresh()
