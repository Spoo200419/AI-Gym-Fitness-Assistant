from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from services.progress_service import get_workout_progress


router = APIRouter()


@router.get("/summary")
def workout_progress(
    db: Session = Depends(get_db)
):

    progress = get_workout_progress(db)

    return {
        "message": "Workout progress calculated successfully.",
        "progress": progress
    }