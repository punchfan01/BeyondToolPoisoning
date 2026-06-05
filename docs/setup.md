# Setup Guide

## Requirements

- Python 3.10+
- [ngrok](https://ngrok.com/) (for exposing local servers to the internet)
- Gmail account with App Password enabled (for Email Exfiltration scenario)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/punchfan01/BeyondToolPoisoning.git
cd BeyondToolPoisoning
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```

| Variable | Description | Used In |
| --- | --- | --- |
| `UPLOAD_URL` | Attacker-controlled Flask server endpoint | file_exfiltration |
| `ATTACKER_EMAIL` | Attacker-controlled email address | email_exfiltration |
| `PUBLIC_DOWNLOAD_BASE` | Public ngrok URL for JPEG download links | image_steganography_resp |

---

## Running the Servers

### ngrok setup

Before running the servers, expose the desired port using ngrok:

```bash
ngrok http {PORT}
```

Copy the generated URL and set it as `PUBLIC_DOWNLOAD_BASE` in your `.env` file.

### Server port reference

Replace `{PORT}` in the ngrok command above with the port number of the server you want to expose.

| Scenario | File | Port |
| --- | --- | --- |
| File Exfiltration (MCP) | `server/passive/file_exfiltration/file_exfiltration.py` | 8000 |
| File Exfiltration (Flask) | `server/passive/file_exfiltration/flask_server.py` | 5000 |
| Email Exfiltration | `server/passive/email_exfiltration/email_exfiltration.py` | 8001 |
| URL Substitution (desc) | `server/active/url_substitution/url_substitution_desc.py` | 8002 |
| URL Substitution (resp) | `server/active/url_substitution/url_substitution_resp.py` | 8003 |
| Code Augmentation (desc) | `server/active/code_augmentation/code_augmentation_desc.py` | 8004 |
| Code Augmentation (resp) | `server/active/code_augmentation/code_augmentation_resp.py` | 8005 |
| Image Steganography (resp) | `server/active/image_steganography/image_steganography_resp.py` | 8006 |
| Image Steganography (desc) | `server/active/image_steganography/image_steganography_desc.py` | 8007 |

### Running a server

Run the server corresponding to the scenario you want to test. The file path for each server is listed in the ‘File’ column of the table above.
For example, to run the File Exfiltration scenario:

```bash
python server/passive/file_exfiltration/file_exfiltration.py
```

---

## MCP Host Configuration

### ChatGPT

1. Go to [chatgpt.com](https://chatgpt.com/)
2. Select **Settings** → **Connectors** → **Advanced Settings**
3. Enable **Developer Mode**
4. Go back to **Connectors** and click **Create**
5. Fill in the following:
    - **Name**: Enter a name (e.g., `FCE`)
    - **MCP Server URL**: Enter the ngrok URL with `/mcp/` path:
        
        ```
        https://{ngrok-url}/mcp/
        ```
        
    - **Authentication**: Select `No Auth`
6. Check **I trust this application** and click **Create**

### Claude Desktop

1. Go to Claude Desktop
2. Select **Customize** → **Connector**
3. Click **+ → Add custom connector**
4. Fill in the following
    - **Name**: Enter a name (e.g., `FCE`)
    - **MCP Server URL**: Enter the ngrok URL with `/mcp/` path:
        
        ```
        https://{ngrok-url}/mcp/
        ```
        
5. Click **Add**

### Gemini CLI

1. Open `.gemini/settings.json`
2. Add the server URL:
    
    ```json
    "mcpServers": {
        {MCP-server-name}: {
          "url": "https://{ngrok-url}/mcp/"
        }
      }
    ```
    

---

## Running Experiments

1. Start the target MCP server
2. Expose it via ngrok and register the URL on the target LLM platform
3. Use the corresponding prompt from `prompts/` for each scenario
4. Replace placeholders (`{SERVER}`, `{TRIAL}`, etc.) before sending

Refer to each prompt file in `prompts/` for platform-specific instructions.