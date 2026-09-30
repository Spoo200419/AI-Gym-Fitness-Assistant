from fastapi import APIRouter

from services.smart_gym_service import get_equipment_status


router = APIRouter()


@router.get("/status")
def smart_gym_status(
    equipment: str = "Treadmill",
    intensity: str = "Moderate"
):

    result = get_equipment_status(
        equipment=equipment,
        intensity=intensity
    )

    return result