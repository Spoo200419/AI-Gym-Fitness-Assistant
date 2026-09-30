from datetime import datetime

from sqlalchemy.orm import Session

from models.workout_result_db import WorkoutResultDB


def save_workout_result(
    db: Session,
    exercise: str,
    target_reps: int,
    completed_reps: int,
    form_feedback: str,
    duration_minutes: float
):

    workout_result = WorkoutResultDB(
        exercise=exercise,
        target_reps=target_reps,
        completed_reps=completed_reps,
        form_feedback=form_feedback,
        duration_minutes=duration_minutes,
        workout_date=datetime.utcnow()
    )

    db.add(workout_result)
    db.commit()
    db.refresh(workout_result)

    return workout_result