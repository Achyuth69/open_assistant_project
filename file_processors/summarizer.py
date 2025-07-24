# summarizer.py
import requests

def summarize_text(text):
    prompt = f"Summarize the following:\n\n{text}\n\nSummary:"
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen:latest",
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "Could not summarize.")
