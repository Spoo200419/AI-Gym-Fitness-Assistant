from fastapi import APIRouter

from services.chatbot import fitness_chatbot


router = APIRouter()


@router.get("/ask")
def ask_chatbot(message: str):

    response = fitness_chatbot(message)

    return response