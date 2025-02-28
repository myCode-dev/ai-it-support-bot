# AI IT Support Chatbot

## 📌 Project Overview

AI IT Support Chatbot is an intelligent IT helpdesk system that allows users to ask IT-related questions via an AI-powered chatbot. If the AI cannot resolve the issue, the system enables users to submit a support ticket for IT personnel to handle.

## 🚀 Tech Stack

- **Frontend**: Vue.js
- **Backend**: Python (FastAPI)
- **API Documentation**: Built-in FastAPI Swagger UI (`/docs`) and Redoc (`/redoc`)
- **Other Technologies**: Please specify (e.g., Redis, WebSocket, Docker, etc.)

## 📂 Project Structure

```
AI-IT-SUPPORT-CHATBOT/
│── backend/                # Backend application
│   │── main.py             # Main backend API entry point
│   │── requirements.txt    # Dependency list
│   │── .env.example        # Example environment variables file
│   │── .env                # Environment variables (ignored in Git)
│   │── faq_data.json       # FAQ storage file (default dataset will be used if missing)
│
│── frontend/               # Frontend application
│   │── src/
│   │   │── assets/         # Static assets (images, CSS)
│   │   │── components/     # Vue components
│   │   │── layouts/        # Layout templates
│   │   │── router/         # Routing
│   │   │── views/          # Page components
│   │   │── App.vue         # Main Vue component
│   │   │── main.js         # Entry point
│   │── public/             # Public static files
│
│── .vscode/                # VS Code settings
│── node_modules/           # Frontend dependencies (ignored)
```

## 🔧 Installation & Execution

### 1️⃣ Backend Setup & Execution

```bash
cd backend
python -m venv venv       # Create virtual environment
source venv/bin/activate  # Activate virtual environment (Windows: venv\Scripts\activate)
pip install -r requirements.txt  # Install dependencies
cp backend/.env.example backend/.env  # Copy example environment file      # Copy example environment file
uvicorn main:app --host 127.0.0.1 --port 8000  # Start FastAPI server
```

### 2️⃣ Frontend Setup & Execution

```bash
cd frontend
npm install              # Install frontend dependencies
npm run serve            # Start frontend server
```

## 📡 API Documentation

This project uses **FastAPI built-in Swagger** for API documentation. After starting the backend server, visit:

- **Swagger UI**: `http://0.0.0.0:8000/docs`
- **Redoc**: `http://127.0.0.1:8000/redoc`

## 📂 FAQ Data Handling

The chatbot loads FAQs from `backend/faq_data.json`. If the file is missing or empty, the system will use a default set of FAQ questions to ensure functionality.

### 🔄 Future Enhancement: Integrating SharePoint List

Currently, the FAQ data is stored in a static JSON file (`faq_data.json`). However, in future implementations, this data source can be replaced with a **SharePoint List** for easier management and real-time updates.

**Proposed Approach:**
1. **Read FAQ data from SharePoint API** using an authenticated request.
2. **Cache the fetched FAQs** locally to reduce API calls.
3. **Modify the backend to dynamically fetch and update FAQ data** instead of reading from `faq_data.json`.

Example code snippet for fetching FAQs from SharePoint:
```python
import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHAREPOINT_API_URL = os.getenv("SHAREPOINT_API_URL")
SHAREPOINT_ACCESS_TOKEN = os.getenv("SHAREPOINT_ACCESS_TOKEN")

def fetch_faq_from_sharepoint():
    headers = {"Authorization": f"Bearer {SHAREPOINT_ACCESS_TOKEN}"}
    response = requests.get(SHAREPOINT_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()  # Convert response to JSON
    else:
        return []  # Return empty list if API call fails
```

To switch from `faq_data.json` to SharePoint, update `main.py` to call `fetch_faq_from_sharepoint()` instead of reading from the static JSON file.

## 🔑 Environment Variables `.env` Configuration

Create a `.env` file in `backend/` by copying the provided `.env.example` file:

```bash
cp backend/.env.example backend/.env
```

### Example `.env.example` file:

```
OPENAI_API_KEY=your_openai_api_key_here
SHAREPOINT_API_URL=your_sharepoint_api_endpoint_here
SHAREPOINT_ACCESS_TOKEN=your_access_token_here
```

Ensure that `.env` is added to `.gitignore` to avoid exposing sensitive credentials.

## 📜 Logging Configuration

To enable logging in `backend/main.py`, add the following:

```python
import logging
from fastapi import FastAPI, Request

app = FastAPI()

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    logging.info(f"Request: {request.method} {request.url} - Response: {response.status_code}")
    return response
```

## 🚀 API Testing Guide

### 1. Start the Backend Server

```bash
cd backend
uvicorn main:app --host 127.0.0.1 --port 8000
```

### 2. Test API (Using curl)

**Test Chatbot**

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"user_id": "12345", "message": "My computer won't start."}'
```

**Test Ticket Submission**

```bash
curl -X POST http://127.0.0.1:8000/ticket -H "Content-Type: application/json" -d '{"user_id": "12345", "issue": "Cannot connect to VPN."}'
```

## 🔗 Additional Notes

- The default homepage (`/`) does not redirect to `/docs`. Please visit `http://127.0.0.1:8000/docs` manually to access the API documentation.
- If running on a remote server, replace `127.0.0.1` with the actual server IP.
- If you encounter issues running the server, ensure `uvicorn` is installed by running:
  ```bash
  pip install uvicorn
  ```

