from pydantic import BaseModel


class EventRequest(BaseModel):
    event_description: str


class ConversationRequest(BaseModel):
    event: str
    interests: str


class FactRequest(BaseModel):
    topic: str
