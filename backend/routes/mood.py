from fastapi import APIRouter

from services.mood_service import analyze_mood


router = APIRouter()


@router.get("/analyze")
def mood_analysis(message: str):

    result = analyze_mood(message)

    return result