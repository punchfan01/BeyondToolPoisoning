import os
import re
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Use the directory where this script is located as the upload folder
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(UPLOAD_FOLDER, "upload_file")
LOG_FILE = os.path.join(UPLOAD_FOLDER, "log_file_exfiltration.txt")

# Create upload folder if it does not exist
os.makedirs(PDF_FOLDER, exist_ok=True)


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename by replacing any character outside alphanumerics,
    Korean characters, and common punctuation with an underscore."""
    return re.sub(r'[^0-9a-zA-Z가-힣._()\- ]', '_', filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    """Receive an uploaded PDF file, save it with a timestamp suffix,
    and append a log entry recording the filename, timestamp, and client IP."""

    # Validate that the request contains the expected file field
    if 'return_file' not in request.files:
        return jsonify({"status": "error", "message": "No file part in request"}), 400

    file = request.files['return_file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    # Sanitize filename and split into name and extension
    original_filename = sanitize_filename(file.filename)
    filename, ext = os.path.splitext(original_filename)

    # Append timestamp (YYYYMMDD_HHMM) to avoid filename collisions
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    new_filename = f"{filename}_{timestamp}{ext}"
    save_path = os.path.join(PDF_FOLDER, new_filename)

    # Save the uploaded file to disk
    file.save(save_path)

    # Record original filename, timestamp, and client IP in the log file
    client_ip = request.remote_addr
    log_entry = f"{original_filename}\n{timestamp}\n{client_ip}\n\n"
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(log_entry)

    return jsonify({
        "status": "success",
        "message": f"File saved to {save_path}",
        "log": log_entry.strip()
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
