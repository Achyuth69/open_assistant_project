# app/ollama_api.py

import requests

def query_ollama(prompt, system_prompt, model="qwen2.5:latest"):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"].strip()
