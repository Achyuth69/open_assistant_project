import streamlit as st
import json
from collections import Counter
from pathlib import Path

# File path
FEEDBACK_FILE = Path("app/feedback_storage.json")

# Load feedback data
def load_feedback():
    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Analytics Logic
feedback_data = load_feedback()
st.set_page_config(page_title="Feedback Analytics", layout="wide")
st.title("📊 Feedback Analytics")
st.caption("Real-time insights from user feedback")

if not feedback_data:
    st.warning("No feedback data found.")
else:
    # Total Feedback
    st.metric("📦 Total Feedback Entries", len(feedback_data))

    # Most Common Feedback
    feedback_counts = Counter(entry["feedback"] for entry in feedback_data)
    most_common = feedback_counts.most_common(1)[0]
    st.metric("🔥 Most Common Feedback", f"{most_common[0]} ({most_common[1]})")

    # Show Recent Feedback
    st.subheader("🕒 Last 5 Feedback Entries")
    for entry in reversed(feedback_data[-5:]):
        st.markdown("---")
        st.markdown(f"**🗨️ Question:** {entry['question']}")
        st.markdown(f"**🤖 Answer:** {entry['answer']}")
        st.markdown(f"**📝 Feedback:** {entry['feedback']}")
