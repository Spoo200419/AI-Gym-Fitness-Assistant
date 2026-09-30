from fastapi import APIRouter
from services.workout_service import generate_workout

router = APIRouter()


@router.get("/recommendation")
def workout_recommendation(
    goal: str,
    experience_level: str
):

    workout = generate_workout(
        goal,
        experience_level
    )

    return workout