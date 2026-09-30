from fastapi import APIRouter
from models.user import UserProfile
from services.fitness_service import calculate_bmi
from services.workout_service import generate_workout

router = APIRouter()


@router.post("/profile")
def create_profile(user: UserProfile):

    # Calculate BMI
    bmi_result = calculate_bmi(
        user.weight,
        user.height
    )

    # Generate workout recommendation
    workout = generate_workout(
        user.goal,
        user.experience_level
    )

    return {
        "profile": user,
        "fitness_analysis": bmi_result,
        "workout_recommendation": workout
    }