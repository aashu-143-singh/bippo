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

    message = data.message.strip()

    if not message:
        return {
            "reply": "I'm listening. Tell me what's on your mind."
        }

    return {
        "reply": "I hear you. Let's take things one step at a time. Tell me a little more about what's on your mind.",
        "mode": "prototype"
    }
