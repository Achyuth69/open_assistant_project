# 💬 Open Assistant — Open-Source AI Chatbot

An open-source AI assistant powered by Qwen2.5 running locally via [Ollama](https://ollama.com), with a beautiful Streamlit UI, system prompt transparency, offline operation, and multilingual readiness (default: English).

---

## 📁 Folder Structure

```bash
open_assistant_project/
│
├── app/
│   ├── main.py
│   ├── prompt_config.py
│   ├── ollama_api.py
│   ├── feedback_storage.json
│   ├── file_processors/
│   │   ├── transcriber.py
│   │   ├── summarizer.py
│   │   ├── media_analyzer.py
│   │   └── drive_handler.py
│
├── assets/
│   └── logo.png  # (optional for branding)
│
├── requirements.txt
├── README.md
└── report.md

---

## 🚀 Features
🧠 Powered by Qwen2.5 via Ollama

💻 100% Offline capable

✨ Modern, smooth Streamlit UI

🗣️ Indic language ready (default: English)

🔁 Persistent chat memory

📥 Upload any file (audio, video, PDF, etc.)

🎧 Audio transcription + summarization

📊 Integrated user feedback system

🔐 Transparent system prompt config

📂 Google Drive file fetch support

📈 Feedback Analytics Page (WIP)

---

## 🧑‍💻 Installation
```bash
# 1. Clone project
git clone https://github.com/yourusername/open_assistant_project
cd open_assistant_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 4. Install all dependencies
pip install -r requirements.txt
```

## 🧠 Setup Ollama + Qwen2.5
```bash
# Install Ollama from https://ollama.com/download
# Then pull the model:
ollama pull qwen2.5
```

## ▶️ Run the Open Assistant
```bash
streamlit run app/main.py
```
## 💬 System Prompt Transparency
```python
# In app/prompt_config.py
SYSTEM_PROMPT = """
You are an open-source AI assistant that communicates clearly...
"""
```

## 📈 Potential Extensions
🗃️ Full Feedback Analytics Page (in development)
🌐 Private LLM switcher (LLaMA 3, Phi-3, Mistral)
🗣️ Voice-to-Voice Chat Loop (Coqui + Whisper)
🧩 Plugin System for Task Execution

---
# 🙋 Why This Project?
This project addresses a growing need for private, offline AI tools that can still offer robust functionality across:
-Education (local learning assistant)
-Research (summarize papers, extract audio insights)
-Accessibility (speech-based input/output)
-Regional Language Support (Indic languages)

## 🔐 Privacy & Ethics
-All operations happen locally
-No user data is sent to the cloud.
-Open-source stack ensures transparency and auditability.

## 👏 Acknowledgements
-Qwen2.5 by Alibaba — for a powerful open-source LLM.
-Whisper by OpenAI — for transcription excellence.
-Streamlit — for making AI interfaces smooth and deployable.
-Ollama — for making local LLM hosting simple.


## 📥 Supported File Uploads
-🎧 Audio files → Transcribed using Whisper
-📹 Video files → Auto audio-extracted + transcribed
-📄 PDFs → Summarized
-🌐 Google Drive files → Paste public link

## 📊 Feedback System
Stores all feedback in app/feedback_storage.json
Includes:
--✅ User message
--🤖 Assistant response
--🌟 Rating (1–5)
-Auto-handles file creation + error recovery
-📈 Analytics Page (optional, coming soon)

---
## 📦 requirements.txt
```bash
streamlit
requests
pydub
whisper
PyPDF2
torch
torchaudio
torchvision
openai
google-auth
google-auth-oauthlib
google-api-python-client
```

---
### 🧠 Default Communication Language
-Default: English
-Support for Indic languages included (future toggle)
-Can be switched via system prompt updates

### 🙌 Credits
-Qwen2.5 by Alibaba (via Ollama)
-Whisper by OpenAI
-Streamlit for frontend
-You — for building open-source AI tools!

### 📃 License
This project is released under the MIT License.
```vbnet
Let me know if you'd like the `report.md` template as well — and I’ll generate that next.
```