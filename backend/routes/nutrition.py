from fastapi import APIRouter

from services.nutrition_service import generate_nutrition_plan


router = APIRouter()


@router.get("/recommendation")
def nutrition_recommendation(
    age: int,
    gender: str,
    height: float,
    weight: float,
    activity_level: str,
    goal: str,
    dietary_preference: str = "vegetarian"
):

    nutrition_plan = generate_nutrition_plan(
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        activity_level=activity_level,
        goal=goal,
        dietary_preference=dietary_preference
    )

    return nutrition_plan