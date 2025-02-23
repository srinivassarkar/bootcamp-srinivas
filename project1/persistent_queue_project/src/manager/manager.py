# import streamlit as st
# from src.queue.sqlite_queue import PersistentQSQLite

# st.title("Queue Manager")

# queue = PersistentQSQLite()
# status = queue.get_status()

# # Add headers for clarity
# st.write("### Jobs")
# col1, col2, col3 = st.columns([3, 1, 1])  # Adjust column widths
# col1.write("Job ID")
# col2.write("Status")
# col3.write("Actions")

# for job in status:
#     col1, col2, col3 = st.columns([3, 1, 1])
#     col1.write(job["id"])
#     col2.write(job["status"])
#     if job["status"] == "FAILED":
#         if col3.button("Resubmit", key=f"resubmit_{job['id']}"):
#             queue.resubmit(job["id"])
#             st.success(f"Resubmitted {job['id']}")
#     if job["status"] in ["PENDING", "FAILED"]:
#         if col3.button("Cancel", key=f"cancel_{job['id']}"):
#             queue.cancel(job["id"])
#             st.success(f"Canceled {job['id']}")



import streamlit as st
import pandas as pd
from src.queue.sqlite_queue import PersistentQSQLite
import time

st.set_page_config(page_title="Queue Manager", layout="wide")

st.title("🚀 Queue Manager")

queue = PersistentQSQLite()
status = queue.get_status()

# Convert to DataFrame for better UI
df = pd.DataFrame(status)

if df.empty:
    st.warning("No jobs found!")
else:
    def get_status_color(status):
        return {
            "COMPLETED": "✅",
            "FAILED": "❌",
            "PENDING": "⏳",
            "RUNNING": "⚡",
        }.get(status, "❓")

    def resubmit_job(job_id):
        queue.resubmit(job_id)
        st.success(f"Resubmitted job {job_id}")
        time.sleep(1)  # Give UI time to update
        st.rerun()

    def cancel_job(job_id):
        queue.cancel(job_id)
        st.success(f"Canceled job {job_id}")
        time.sleep(1)  
        st.rerun()

    # Create Table Layout
    st.markdown("### Job Queue")
    for _, row in df.iterrows():
        col1, col2, col3 = st.columns([3, 2, 2])
        col1.write(f"**Job ID:** {row['id']}")
        col2.write(f"**Status:** {get_status_color(row['status'])} {row['status']}")

        with col3:
            if row["status"] == "FAILED":
                st.button("🔄 Resubmit", key=f"resubmit_{row['id']}", on_click=resubmit_job, args=(row["id"],))
            if row["status"] in ["PENDING", "FAILED"]:
                st.button("🛑 Cancel", key=f"cancel_{row['id']}", on_click=cancel_job, args=(row["id"],))
    
st.markdown("---")
st.info("✅ **Live updates enabled** – Job status updates when you take actions!")
