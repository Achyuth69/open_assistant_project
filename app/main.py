import streamlit as st
from prompt_config import get_system_prompt
from ollama_api import query_ollama
import json
from pathlib import Path
import os
import tempfile
import whisper
from PyPDF2 import PdfReader

# ====== Feedback Storage Helper ====== #
FEEDBACK_FILE = Path("app/feedback_storage.json")

def save_feedback(question, answer, feedback):
    feedback_entry = {"question": question, "answer": answer, "feedback": feedback}
    if FEEDBACK_FILE.exists():
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    data.append(feedback_entry)
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ====== Page Setup ====== #
st.set_page_config(page_title="Open Assistant", layout="wide")
st.title("💬 Open-Source AI Assistant")
st.caption("Powered by Qwen2.5 via Ollama · Works Offline 🚀")

# ====== File Upload Section ====== #
st.sidebar.header("📂 Upload Any File")
uploaded_file = st.sidebar.file_uploader("Upload file (PDF, audio, video, image, docx, etc.)", type=None)

if uploaded_file:
    file_details = {
        "filename": uploaded_file.name,
        "type": uploaded_file.type,
        "size": uploaded_file.size,
    }
    st.sidebar.success(f"✅ Uploaded: {uploaded_file.name}")
    st.sidebar.json(file_details)

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if uploaded_file.type.startswith(("audio", "video")):
        st.info("🔊 Transcribing with Whisper...")
        model = whisper.load_model("base")
        result = model.transcribe(tmp_path)
        transcription = result["text"]
        st.success("📝 Transcription:")
        st.write(transcription)
        st.session_state.chat_history.append({"role": "system", "content": transcription})

    elif uploaded_file.type == "application/pdf":
        st.info("📄 Reading PDF...")
        pdf = PdfReader(tmp_path)
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        st.success("📑 Extracted Text:")
        st.write(text[:2000] if text else "❌ Could not extract text from this PDF.")
        st.session_state.chat_history.append({"role": "system", "content": text})

    else:
        st.warning("📁 Uploaded file stored, but not auto-processed (custom logic needed).")

# ====== Google Drive or File Link Input ====== #
with st.sidebar.expander("🔗 Or Paste Google Drive / File Link"):
    drive_url = st.text_input("Enter Drive or File URL")
    if drive_url:
        st.sidebar.info("Received Link:")
        st.sidebar.write(drive_url)
        # TODO: You can implement downloading and analysis later.

# ====== Chat History Setup ====== #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_user_input" not in st.session_state:
    st.session_state.last_user_input = None
if "last_response" not in st.session_state:
    st.session_state.last_response = None

# ====== Show Previous Chat Messages ====== #
for entry in st.session_state.chat_history:
    st.chat_message(entry["role"]).write(entry["content"])

# ====== User Chat Input ====== #
user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.last_user_input = user_input

    try:
        system_prompt = get_system_prompt()
        response = query_ollama(user_input, system_prompt, model="qwen2.5:latest")
        st.chat_message("assistant").write(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.session_state.last_response = response

    except Exception as e:
        st.error(f"❌ Error while generating response: {e}")

# ====== Feedback Submission Section ====== #
if st.session_state.last_user_input and st.session_state.last_response:
    with st.expander("📝 Was this response helpful?"):
        feedback = st.radio(
            "Your Feedback:",
            ["👍 Helpful", "👎 Not Useful", "🤔 Neutral", "🚫 Wrong"],
            key="feedback_radio",
            horizontal=True
        )
        if st.button("Submit Feedback"):
            save_feedback(
                st.session_state.last_user_input,
                st.session_state.last_response,
                feedback,
            )
            st.success("✅ Feedback saved!")
            st.session_state.last_user_input = None
            st.session_state.last_response = None
