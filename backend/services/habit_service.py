from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from models.workout_result_db import WorkoutResultDB


def get_habit_analysis(db: Session):

    results = (
        db.query(WorkoutResultDB)
        .order_by(
            WorkoutResultDB.id.desc()
        )
        .all()
    )

    total_workouts = len(results)

    # --------------------------------------------------
    # NO WORKOUT HISTORY
    # --------------------------------------------------

    if total_workouts == 0:

        return {
            "habit_status": "No workout history",
            "total_workouts": 0,
            "workout_days": 0,
            "workout_frequency": 0,
            "current_streak": 0,
            "consistency_percentage": 0,
            "behavior_analysis": (
                "Start recording workouts "
                "to analyze your fitness habits."
            ),
            "recommendation": (
                "Complete your first workout "
                "and maintain a regular schedule."
            ),
            "motivational_nudge": (
                "Every workout is a step forward! 💪"
            )
        }


    # --------------------------------------------------
    # GET WORKOUT DATES
    # --------------------------------------------------

    workout_dates = set()

    for result in results:

        if result.workout_date is not None:

            workout_dates.add(
                result.workout_date.date()
            )


    # --------------------------------------------------
    # OLD RECORD COMPATIBILITY
    # --------------------------------------------------

    # Existing workout records may not have a date
    # because workout_date was added later.

    if len(workout_dates) == 0:

        return {
            "habit_status": "Tracking Started",

            "total_workouts": total_workouts,

            "workout_days": 0,

            "workout_frequency": 0,

            "current_streak": 0,

            "consistency_percentage": 0,

            "behavior_analysis": (
                "Your previous workout records are available, "
                "but their dates were recorded before habit "
                "tracking was added."
            ),

            "recommendation": (
                "Continue completing workouts. New workouts "
                "will automatically be recorded with dates "
                "for habit and consistency analysis."
            ),

            "motivational_nudge": (
                "Great start! Keep exercising and build "
                "your fitness habit. 💪🔥"
            )
        }


    # --------------------------------------------------
    # CURRENT STREAK
    # --------------------------------------------------

    today = datetime.utcnow().date()

    current_streak = 0

    check_date = today

    while check_date in workout_dates:

        current_streak += 1

        check_date = (
            check_date - timedelta(days=1)
        )


    # If there was no workout today,
    # check yesterday.

    if current_streak == 0:

        check_date = (
            today - timedelta(days=1)
        )

        while check_date in workout_dates:

            current_streak += 1

            check_date = (
                check_date - timedelta(days=1)
            )


    # --------------------------------------------------
    # WORKOUT FREQUENCY
    # --------------------------------------------------

    first_date = min(workout_dates)

    last_date = max(workout_dates)

    days_active_period = (
        last_date - first_date
    ).days + 1

    if days_active_period > 0:

        workout_frequency = (
            len(workout_dates) /
            days_active_period
        )

    else:

        workout_frequency = len(workout_dates)


    # --------------------------------------------------
    # CONSISTENCY
    # --------------------------------------------------

    if days_active_period > 0:

        consistency_percentage = (
            len(workout_dates) /
            days_active_period
        ) * 100

    else:

        consistency_percentage = 100


    consistency_percentage = round(
        min(consistency_percentage, 100),
        2
    )


    # --------------------------------------------------
    # BEHAVIOR ANALYSIS
    # --------------------------------------------------

    if consistency_percentage >= 70:

        habit_status = "Highly Consistent"

        behavior_analysis = (
            "Your workout pattern shows strong "
            "consistency and regular exercise behavior."
        )

        recommendation = (
            "Maintain your current routine and "
            "gradually increase workout intensity."
        )

        motivational_nudge = (
            "Excellent consistency! Keep the streak going! 🔥"
        )

    elif consistency_percentage >= 40:

        habit_status = "Moderately Consistent"

        behavior_analysis = (
            "You are exercising regularly, but "
            "there are some gaps in your workout routine."
        )

        recommendation = (
            "Try scheduling workouts on fixed days "
            "to improve consistency."
        )

        motivational_nudge = (
            "You're making progress! A little more consistency "
            "can make a big difference. 💪"
        )

    else:

        habit_status = "Needs Improvement"

        behavior_analysis = (
            "Your workout history shows irregular "
            "exercise patterns."
        )

        recommendation = (
            "Start with short workouts and create "
            "a simple weekly exercise schedule."
        )

        motivational_nudge = (
            "Don't give up! Start small and build your routine. 🌟"
        )


    # --------------------------------------------------
    # RETURN RESULT
    # --------------------------------------------------

    return {

        "habit_status": habit_status,

        "total_workouts": total_workouts,

        "workout_days": len(workout_dates),

        "workout_frequency": round(
            workout_frequency,
            2
        ),

        "current_streak": current_streak,

        "consistency_percentage": (
            consistency_percentage
        ),

        "behavior_analysis": behavior_analysis,

        "recommendation": recommendation,

        "motivational_nudge": motivational_nudge
    }