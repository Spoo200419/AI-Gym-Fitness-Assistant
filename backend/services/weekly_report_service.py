from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from models.workout_result_db import WorkoutResultDB


def get_weekly_report(db: Session):

    # --------------------------------------------------
    # CURRENT WEEK
    # --------------------------------------------------

    today = datetime.utcnow().date()

    start_of_week = (
        today - timedelta(days=today.weekday())
    )

    end_of_week = (
        start_of_week + timedelta(days=6)
    )


    # --------------------------------------------------
    # GET ALL WORKOUT RESULTS
    # --------------------------------------------------

    results = (
        db.query(WorkoutResultDB)
        .all()
    )


    # --------------------------------------------------
    # FILTER THIS WEEK'S DATED WORKOUTS
    # --------------------------------------------------

    weekly_results = []

    for result in results:

        if result.workout_date is not None:

            workout_date = result.workout_date.date()

            if (
                start_of_week
                <= workout_date
                <= end_of_week
            ):

                weekly_results.append(result)


    # --------------------------------------------------
    # OLD RECORD COMPATIBILITY
    # --------------------------------------------------

    if len(weekly_results) == 0:

        return {

            "report_period": (
                f"{start_of_week} to {end_of_week}"
            ),

            "weekly_workouts": 0,

            "total_reps": 0,

            "total_duration_minutes": 0,

            "performance_score": 0,

            "exercise_statistics": {},

            "consistency_percentage": 0,

            "summary": (
                "No dated workouts were recorded "
                "during the current week."
            ),

            "improvement_recommendation": (
                "Complete workouts during the week "
                "to generate a personalized weekly report."
            )
        }


    # --------------------------------------------------
    # BASIC STATISTICS
    # --------------------------------------------------

    total_workouts = len(weekly_results)

    total_reps = sum(
        result.completed_reps
        for result in weekly_results
    )

    total_duration = sum(
        result.duration_minutes
        for result in weekly_results
    )


    # --------------------------------------------------
    # PERFORMANCE SCORE
    # --------------------------------------------------

    total_target_reps = sum(
        result.target_reps
        for result in weekly_results
    )

    if total_target_reps > 0:

        performance_score = (
            total_reps /
            total_target_reps
        ) * 100

    else:

        performance_score = 0


    performance_score = round(
        min(performance_score, 100),
        2
    )


    # --------------------------------------------------
    # UNIQUE WORKOUT DAYS
    # --------------------------------------------------

    workout_days = set()

    for result in weekly_results:

        workout_days.add(
            result.workout_date.date()
        )

    number_of_workout_days = len(
        workout_days
    )


    # --------------------------------------------------
    # WEEKLY CONSISTENCY
    # --------------------------------------------------

    consistency_percentage = (
        number_of_workout_days / 7
    ) * 100

    consistency_percentage = round(
        consistency_percentage,
        2
    )


    # --------------------------------------------------
    # EXERCISE STATISTICS
    # --------------------------------------------------

    exercise_statistics = {}

    for result in weekly_results:

        exercise = result.exercise

        if exercise not in exercise_statistics:

            exercise_statistics[exercise] = {

                "workouts": 0,

                "total_reps": 0,

                "total_duration_minutes": 0
            }


        exercise_statistics[
            exercise
        ]["workouts"] += 1


        exercise_statistics[
            exercise
        ]["total_reps"] += result.completed_reps


        exercise_statistics[
            exercise
        ]["total_duration_minutes"] += (
            result.duration_minutes
        )


    # Round exercise durations

    for exercise in exercise_statistics:

        exercise_statistics[
            exercise
        ]["total_duration_minutes"] = round(
            exercise_statistics[
                exercise
            ]["total_duration_minutes"],
            2
        )


    # --------------------------------------------------
    # WEEKLY SUMMARY
    # --------------------------------------------------

    if performance_score >= 80:

        summary = (
            "Excellent weekly performance! "
            "Your workout completion and consistency "
            "are strong."
        )

        recommendation = (
            "Maintain your routine and gradually "
            "increase workout difficulty."
        )

    elif performance_score >= 50:

        summary = (
            "Good progress this week. "
            "There is room to improve workout completion "
            "and consistency."
        )

        recommendation = (
            "Try to complete your planned repetitions "
            "and maintain a regular weekly schedule."
        )

    else:

        summary = (
            "Your weekly workout activity is still "
            "developing."
        )

        recommendation = (
            "Start with short, manageable workouts "
            "and gradually build consistency."
        )


    # --------------------------------------------------
    # RETURN REPORT
    # --------------------------------------------------

    return {

        "report_period": (
            f"{start_of_week} to {end_of_week}"
        ),

        "weekly_workouts": total_workouts,

        "workout_days": number_of_workout_days,

        "total_reps": total_reps,

        "total_duration_minutes": round(
            total_duration,
            2
        ),

        "performance_score": performance_score,

        "consistency_percentage": (
            consistency_percentage
        ),

        "exercise_statistics": (
            exercise_statistics
        ),

        "summary": summary,

        "improvement_recommendation": (
            recommendation
        )
    }