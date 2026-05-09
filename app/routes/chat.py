from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.services.recommendation_service import process_chat

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return process_chat(request.messages)
