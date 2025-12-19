from fastapi import APIRouter
from pydantic import BaseModel
from app.agent import run_agent

router = APIRouter(prefix="/api")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = run_agent(req.message)
    return {"reply": reply}
