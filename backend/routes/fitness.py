from fastapi import APIRouter
from services.fitness_service import calculate_bmi

router = APIRouter()


@router.get("/bmi")
def bmi(weight: float, height: float):

    result = calculate_bmi(weight, height)

    return result