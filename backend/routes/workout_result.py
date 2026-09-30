from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.workout_result import WorkoutResult
from models.workout_result_db import WorkoutResultDB
from services.workout_result_service import save_workout_result


router = APIRouter()


@router.post("/result")
def create_workout_result(
    result: WorkoutResult,
    db: Session = Depends(get_db)
):

    workout_result = save_workout_result(
        db=db,
        exercise=result.exercise,
        target_reps=result.target_reps,
        completed_reps=result.completed_reps,
        form_feedback=result.form_feedback,
        duration_minutes=result.duration_minutes
    )

    return {
        "message": "Workout result saved successfully.",
        "workout_result": {
            "id": workout_result.id,
            "exercise": workout_result.exercise,
            "target_reps": workout_result.target_reps,
            "completed_reps": workout_result.completed_reps,
            "form_feedback": workout_result.form_feedback,
            "duration_minutes": workout_result.duration_minutes
        }
    }


@router.get("/results")
def get_workout_results(
    db: Session = Depends(get_db)
):

    results = db.query(WorkoutResultDB).all()

    return {
        "total_results": len(results),
        "workout_results": [
            {
                "id": result.id,
                "exercise": result.exercise,
                "target_reps": result.target_reps,
                "completed_reps": result.completed_reps,
                "form_feedback": result.form_feedback,
                "duration_minutes": result.duration_minutes
            }
            for result in results
        ]
    }


@router.get("/results/{exercise_name}")
def get_results_by_exercise(
    exercise_name: str,
    db: Session = Depends(get_db)
):

    results = (
        db.query(WorkoutResultDB)
        .filter(
            WorkoutResultDB.exercise.ilike(exercise_name)
        )
        .all()
    )

    return {
        "exercise": exercise_name,
        "total_results": len(results),
        "workout_results": [
            {
                "id": result.id,
                "exercise": result.exercise,
                "target_reps": result.target_reps,
                "completed_reps": result.completed_reps,
                "form_feedback": result.form_feedback,
                "duration_minutes": result.duration_minutes
            }
            for result in results
        ]
    }