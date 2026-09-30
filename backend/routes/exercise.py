from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from services.workout_result_service import save_workout_result
from services.exercise_service import get_exercise


router = APIRouter()


@router.get("/list")
def list_exercises():

    return {
        "exercises": [
            "squat",
            "pushup",
            "lunge",
            "glute bridge",
            "plank"
        ]
    }


@router.get("/start/squat")
def start_squat_detection(
    db: Session = Depends(get_db)
):

    try:

        from ai.squat_detector import detect_squat

        # Start AI squat detection
        completed_reps, duration_minutes = detect_squat()

        target_reps = 10

        if completed_reps is None:
            completed_reps = 0

        if completed_reps >= target_reps:

            form_feedback = "Workout completed"

        else:

            form_feedback = "Workout incomplete"

        # Save workout result
        workout_result = save_workout_result(
            db=db,
            exercise="Squat",
            target_reps=target_reps,
            completed_reps=completed_reps,
            form_feedback=form_feedback,
            duration_minutes=duration_minutes
        )

        return {
            "message": "Squat detection completed and result saved.",
            "workout_result": {
                "id": workout_result.id,
                "exercise": workout_result.exercise,
                "target_reps": workout_result.target_reps,
                "completed_reps": workout_result.completed_reps,
                "form_feedback": workout_result.form_feedback,
                "duration_minutes": workout_result.duration_minutes
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/start/pushup")
def start_pushup_detection(
    db: Session = Depends(get_db)
):

    try:

        from ai.pushup_detector import detect_pushup

        # Start AI push-up detection
        completed_reps, duration_minutes = detect_pushup()

        target_reps = 10

        if completed_reps is None:
            completed_reps = 0

        if completed_reps >= target_reps:

            form_feedback = "Workout completed"

        else:

            form_feedback = "Workout incomplete"

        # Save workout result into database
        workout_result = save_workout_result(
            db=db,
            exercise="Push-up",
            target_reps=target_reps,
            completed_reps=completed_reps,
            form_feedback=form_feedback,
            duration_minutes=duration_minutes
        )

        return {
            "message": "Push-up detection completed and result saved.",
            "workout_result": {
                "id": workout_result.id,
                "exercise": workout_result.exercise,
                "target_reps": workout_result.target_reps,
                "completed_reps": workout_result.completed_reps,
                "form_feedback": workout_result.form_feedback,
                "duration_minutes": workout_result.duration_minutes
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{exercise_name}")
def exercise_details(exercise_name: str):

    exercise = get_exercise(exercise_name)

    if exercise is None:

        raise HTTPException(
            status_code=404,
            detail="Exercise not found"
        )

    return exercise