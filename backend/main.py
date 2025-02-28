from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
import json
import random
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fuzzywuzzy import process

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
openai.api_key = os.getenv("OPENAI_API_KEY")



# 📂 **load FAQ JSON**
# Define the path to faq_data.json
FAQ_FILE_PATH = "backend/faq_data.json"

# Function to load FAQs from JSON
def load_faq_data():
    if os.path.exists(FAQ_FILE_PATH) and os.path.getsize(FAQ_FILE_PATH) > 0:
        try:
            with open(FAQ_FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading FAQ data: {e}")
            return []
    else:
        print("FAQ file missing or empty. Using default FAQ data.")
        return [
            {"question": "How do I reset my password?", "answer": "Go to Settings -> Security -> Reset Password."},
            {"question": "My VPN is not working, what should I do?", "answer": "Restart your computer and try again."},
            {"question": "How do I request a new laptop?", "answer": "Submit an IT request ticket via the IT Support Portal."}
        ]

faq_data = load_faq_data()

user_sessions = {}

tickets = []

def check_faq(question):
    questions = [faq["question"] for faq in faq_data]
    best_match, score = process.extractOne(question, questions)
    if score > 70:
        return next(faq["answer"] for faq in faq_data if faq["question"] == best_match)
    return None

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat(query: ChatRequest):
    user_id = query.user_id
    question = query.message

    if user_id not in user_sessions:
        user_sessions[user_id] = []

    faq_answer = check_faq(question)
    if faq_answer:
        return {"response": faq_answer, "suggest_ticket": False}

    messages = [{"role": "system", "content": "You are an IT support assistant."}]
    messages += user_sessions[user_id][-5:]  

    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return {"response": response.choices[0].message["content"]}

    user_sessions[user_id].append({"role": "user", "content": question})
    user_sessions[user_id].append({"role": "assistant", "content": bot_response})

    suggest_ticket = "contact IT support" in bot_response.lower() or "unable to help" in bot_response.lower()

    return {"response": bot_response, "suggest_ticket": suggest_ticket}

class TicketRequest(BaseModel):
    user_id: str
    issue: str

@app.post("/ticket")
async def create_ticket(ticket: TicketRequest):
    ticket_id = random.randint(1000, 9999)
    new_ticket = {
        "ticket_id": ticket_id,
        "user_id": ticket.user_id,
        "issue": ticket.issue,
        "status": "submitted"
    }
    tickets.append(new_ticket)
    return new_ticket

@app.get("/tickets")
async def get_tickets():
    return tickets

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run(app, host="127.0.0.1", port=port)
