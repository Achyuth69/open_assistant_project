# drive_handler.py
import gdown

def download_drive_file(drive_url, output_path="downloads/temp_file"):
    try:
        gdown.download(drive_url, output=output_path, quiet=False, fuzzy=True)
        return output_path
    except Exception as e:
        return f"Error downloading: {str(e)}"
