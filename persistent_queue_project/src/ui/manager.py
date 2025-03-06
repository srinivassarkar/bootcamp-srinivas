# src/ui/manager.py
"""Streamlit UI for managing job queue with crash detection."""

import os
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from src.jobqueue import PersistentQInterface, get_queue

load_dotenv()
MANAGER_PASSWORD = os.getenv("MANAGER_PASSWORD")  # Default fallback

st.set_page_config(page_title="Queue Manager", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Enter Password", type="password")
    if password == MANAGER_PASSWORD:
        st.session_state.authenticated = True
        st.success("Logged in successfully!")
    else:
        st.error("Incorrect password")
        st.stop()

st.title("🚀 Queue Manager")

queue: PersistentQInterface = get_queue()
status = queue.get_status()

# Auto-detect stalled jobs
df = pd.DataFrame(status)
stale_jobs = df[(df["status"] == "PROCESSING") & 
                (df["last_heartbeat"] < (datetime.now() - timedelta(minutes=5)).isoformat())]
if not stale_jobs.empty:
    st.warning(f"Detected {len(stale_jobs)} stalled jobs!")

if st.button("🔍 Check Stalled Jobs", key="check_stalled"):
    queue.check_stalled_jobs()
    st.success("Checked stalled jobs; requeued if needed.")
    st.rerun()

if df.empty:
    st.warning("No jobs in queue!")
else:
    def get_status_emoji(status: str) -> str:
        """Map job status to emoji."""
        return {
            "COMPLETED": "✅", "FAILED": "❌", "PENDING": "⏳",
            "PROCESSING": "⚡", "UNPROCESSABLE": "🚫", "CANCELED": "🗑️"
        }.get(status, "❓")

    def resubmit_job(job_id: str) -> None:
        queue.resubmit(job_id)
        st.success(f"Resubmitted {job_id}")
        st.rerun()

    def cancel_job(job_id: str) -> None:
        queue.cancel(job_id)
        st.success(f"Canceled {job_id}")
        st.rerun()

    st.markdown("### Job Queue")
    col_headers = st.columns([3, 1, 1, 1, 1, 1])
    col_headers[0].write("**Job ID**")
    col_headers[1].write("**Status**")
    col_headers[2].write("**Retries**")
    col_headers[3].write("**Consumer**")
    col_headers[4].write("**Last Heartbeat**")
    col_headers[5].write("**Actions**")

    for _, row in df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([3, 1, 1, 1, 1, 1])
        col1.write(row["id"])
        col2.write(f"{get_status_emoji(row['status'])} {row['status']}")
        col3.write(row.get("retries", 0))
        col4.write(row.get("consumer_id", "N/A"))
        col5.write(row.get("last_heartbeat", "N/A"))
        with col6:
            job_id_hash = hash(row["id"])
            if row["status"] == "FAILED":
                st.button("🔄 Resubmit", key=f"resubmit_{job_id_hash}", on_click=resubmit_job, args=(row["id"],))
            if row["status"] in ["PENDING", "FAILED", "UNPROCESSABLE"]:
                st.button("🛑 Cancel", key=f"cancel_{job_id_hash}", on_click=cancel_job, args=(row["id"],))

st.markdown("---")
st.info("✅ Auto-detects stalled jobs; click 'Check Stalled Jobs' to requeue manually.")