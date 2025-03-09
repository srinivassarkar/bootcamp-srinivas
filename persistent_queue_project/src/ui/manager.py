# src/ui/manager.py
"""Streamlit UI for managing job queue with crash detection."""

import os
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from src.jobqueue import PersistentQInterface, get_queue

load_dotenv()
MANAGER_PASSWORD = os.getenv("MANAGER_PASSWORD", "secure123")

st.set_page_config(page_title="Queue Manager", layout="wide", initial_sidebar_state="collapsed")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "refresh_count" not in st.session_state:
    st.session_state.refresh_count = 0
if "job_history" not in st.session_state:
    st.session_state.job_history = pd.DataFrame()

# Login screen
if not st.session_state.authenticated:
    st.title("🔒 Queue Manager Login")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if password == MANAGER_PASSWORD:
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Incorrect password")
    st.stop()

# Main UI after login
st.title("🚀 Queue Manager")

queue: PersistentQInterface = get_queue()
status = queue.get_status()

df = pd.DataFrame(status)
if not df.empty:
    df["Stalled"] = df.apply(
        lambda row: "⚠️ Stalled"
        if row["status"] == "PROCESSING"
        and row["last_heartbeat"]
        and datetime.fromisoformat(row["last_heartbeat"]) < datetime.now() - timedelta(seconds=30)
        else "",
        axis=1,
    )
    df["consumer_id"] = df["consumer_id"].fillna("N/A")
    df["last_heartbeat"] = df["last_heartbeat"].fillna("N/A")
    if "retries" not in df.columns:
        df["retries"] = 0
    st.session_state.job_history = pd.concat([st.session_state.job_history, df]).drop_duplicates(
        subset=["id"], keep="last"
    )

if st.button("🔍 Check Stalled Jobs", key="check_stalled"):
    queue.check_stalled_jobs()
    st.success("Checked stalled jobs; requeued if needed.")
    st.rerun()

# Filter by status
status_options = [
    "All",
    "PENDING",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "UNPROCESSABLE",
    "CANCELED",
]
selected_status = st.selectbox("Filter by Status", status_options, index=0)
filtered_jobs = (
    st.session_state.job_history
    if selected_status == "All"
    else st.session_state.job_history[st.session_state.job_history["status"] == selected_status]
)

# Auto-refresh every ~5s
st.session_state.refresh_count += 1
if st.session_state.refresh_count % 5 == 0:
    st.rerun()

if filtered_jobs.empty:
    st.warning(f"No jobs found for status: {selected_status}")
else:

    def get_status_emoji(status: str) -> str:
        return {
            "COMPLETED": "✅",
            "FAILED": "❌",
            "PENDING": "⏳",
            "PROCESSING": "⚡",
            "UNPROCESSABLE": "🚫",
            "CANCELED": "🗑️",
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
    col_headers = st.columns([3, 1, 1, 1, 1, 1, 1])
    col_headers[0].write("**Job ID**")
    col_headers[1].write("**Status**")
    col_headers[2].write("**Retries**")
    col_headers[3].write("**Consumer**")
    col_headers[4].write("**Last Heartbeat**")
    col_headers[5].write("**Stalled**")
    col_headers[6].write("**Actions**")

    for _, row in filtered_jobs.iterrows():
        cols = st.columns([3, 1, 1, 1, 1, 1, 1])
        cols[0].write(row["id"])
        cols[1].write(f"{get_status_emoji(row['status'])} {row['status']}")
        cols[2].write(row.get("retries", 0))
        cols[3].write(row["consumer_id"])
        cols[4].write(row["last_heartbeat"])
        cols[5].write(row.get("Stalled", ""))
        with cols[6]:
            job_id_hash = hash(row["id"])
            if row["status"] == "FAILED":
                st.button(
                    "🔄 Resubmit",
                    key=f"resubmit_{job_id_hash}",
                    on_click=resubmit_job,
                    args=(row["id"],),
                )
            if row["status"] in ["PENDING", "FAILED", "UNPROCESSABLE"]:
                st.button(
                    "🛑 Cancel", key=f"cancel_{job_id_hash}", on_click=cancel_job, args=(row["id"],)
                )

st.markdown("---")
st.info("✅ Auto-detects stalled jobs every 10s; requeues after 30s.")
