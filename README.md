# AI IT Support Chatbot

## 📌 Project Overview
AI IT Support Chatbot is an intelligent IT helpdesk system that allows users to ask IT-related questions via an AI-powered chatbot. If the AI cannot resolve the issue, the system enables users to submit a support ticket for IT personnel to handle.

## 🚀 Tech Stack
- **Frontend**: Vue.js
- **Backend**: Python (FastAPI)
- **API Documentation**: Built-in FastAPI Swagger UI (`/docs`) and Redoc (`/redoc`)

## 📂 Project Structure
```
AI-IT-SUPPORT-CHATBOT/
│── backend/                # Backend application
│   │── main.py             # Main backend API entry point
│   │── requirements.txt    # Dependency list
│   │── .env                # Environment variables
│   │── faq_data.json       # FAQ storage file
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

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **Redoc**: `http://127.0.0.1:8000/redoc`

## 🔑 Environment Variables `.env` Configuration
Create a `.env` file in `backend/` with the following variables:
```
OPENAI_API_KEY=your_openai_api_key_here
PORT=8000
```

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
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"user_id": "1", "message": "My computer won't start."}'
```

**Test Ticket Submission**
```bash
curl -X POST http://127.0.0.1:8000/ticket -H "Content-Type: application/json" -d '{"user_id": "1", "issue": "Cannot connect to VPN."}'
```

