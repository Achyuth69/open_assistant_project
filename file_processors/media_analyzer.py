# media_analyzer.py
import os
from moviepy.editor import VideoFileClip, AudioFileClip

def analyze_file(file_path):
    if file_path.lower().endswith((".mp4", ".mov", ".webm")):
        clip = VideoFileClip(file_path)
        return {
            "duration": clip.duration,
            "fps": clip.fps,
            "size": clip.size,
            "audio": clip.audio is not None,
            "type": "video"
        }
    elif file_path.lower().endswith((".mp3", ".wav", ".m4a")):
        clip = AudioFileClip(file_path)
        return {
            "duration": clip.duration,
            "type": "audio"
        }
    else:
        return {"error": "Unsupported file format"}
