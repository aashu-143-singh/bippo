
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Bippo AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    history: list = []

@app.get("/")
def home():
    return {"status": "Bippo brain is online"}

@app.post("/chat")
def chat(data: ChatRequest):

    message = data.message.strip().lower()

    if not message:
        reply = "I'm listening. Tell me what's on your mind."

    elif any(word in message for word in ["sad", "upset", "dukhi", "udaas"]):
        reply = "I'm sorry you're feeling this way. Kya hua? Agar comfortable ho, toh mujhe bata sakte ho."

    elif any(word in message for word in ["happy", "khush", "excited"]):
        reply = "That's lovely! Kya achhi baat hui aaj?"

    elif any(word in message for word in ["stress", "tension", "anxious", "worried"]):
        reply = "It sounds like things feel overwhelming right now. Chalo, ek baar mein ek hi problem par focus karte hain. Sabse zyada tension kis baat ki hai?"

    elif any(word in message for word in ["hello", "hi", "hey"]):
        reply = "Hey! I'm Bippo. How are you feeling today?"

    elif any(word in message for word in ["lonely", "alone", "akela"]):
        reply = "Feeling lonely can be difficult. Kya aaj kuch hua, ya bas aisa feel ho raha hai?"

    elif any(word in message for word in ["thank you", "thanks"]):
        reply = "You're welcome! I'm glad you shared your thoughts with me."

    else:
        reply = "I hear you. Can you tell me a little more about it? I'm here to listen."

    return {
        "reply": reply,
        "mode": "prototype"
    }
