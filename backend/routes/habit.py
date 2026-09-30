from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db

from services.habit_service import get_habit_analysis


router = APIRouter()


@router.get("/summary")
def habit_summary(
    db: Session = Depends(get_db)
):

    habit_data = get_habit_analysis(db)

    return {
        "message": (
            "Fitness habit analysis "
            "calculated successfully."
        ),
        "habit_analysis": habit_data
    }