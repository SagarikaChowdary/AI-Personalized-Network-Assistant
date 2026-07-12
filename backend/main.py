from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.event_analyzer import analyze_event
from backend.fact_checker import fact_check
from backend.conversation_generator import generate_conversation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Event Analyzer
# ----------------------------


class EventRequest(BaseModel):
    event_description: str


@app.post("/analyze-event")
def analyze(request: EventRequest):
    result = analyze_event(request.event_description)
    return {
        "themes": result
    }


# ----------------------------
# Conversation Generator
# ----------------------------

class ConversationRequest(BaseModel):
    event: str
    interests: str


@app.post("/generate-conversation")
def conversation(request: ConversationRequest):
    result = generate_conversation(
        request.event,
        request.interests
    )

    return {
        "conversation": result
    }


# ----------------------------
# Fact Checker
# ----------------------------

class FactRequest(BaseModel):
    topic: str


@app.post("/fact-check")
def fact_checker(request: FactRequest):
    result = fact_check(request.topic)

    return {
        "summary": result
    }
