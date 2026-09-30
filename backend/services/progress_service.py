from sqlalchemy.orm import Session

from models.workout_result_db import WorkoutResultDB


def get_workout_progress(db: Session):

    results = db.query(WorkoutResultDB).all()

    total_workouts = len(results)

    total_reps = sum(
        result.completed_reps
        for result in results
    )

    total_duration = sum(
        result.duration_minutes
        for result in results
    )

    completed_workouts = sum(
        1
        for result in results
        if result.completed_reps >= result.target_reps
    )

    incomplete_workouts = (
        total_workouts - completed_workouts
    )

    if total_workouts > 0:
        average_reps = total_reps / total_workouts
    else:
        average_reps = 0

    # Calculate performance score
    if total_workouts > 0:
        completion_score = (
            total_reps /
            sum(result.target_reps for result in results)
        ) * 100
    else:
        completion_score = 0

    performance_score = round(
        min(completion_score, 100),
        2
    )

    exercise_statistics = {}

    for result in results:

        exercise = result.exercise

        if exercise not in exercise_statistics:

            exercise_statistics[exercise] = {
                "workouts": 0,
                "total_reps": 0,
                "total_duration_minutes": 0
            }

        exercise_statistics[exercise]["workouts"] += 1

        exercise_statistics[exercise]["total_reps"] += (
            result.completed_reps
        )

        exercise_statistics[exercise]["total_duration_minutes"] += (
            result.duration_minutes
        )

    return {
        "total_workouts": total_workouts,
        "total_completed_reps": total_reps,
        "total_workout_duration_minutes": round(
            total_duration,
            2
        ),
        "completed_workouts": completed_workouts,
        "incomplete_workouts": incomplete_workouts,
        "average_reps_per_workout": round(
            average_reps,
            2
        ),
        "performance_score": performance_score,
        "exercise_statistics": exercise_statistics
    }