def generate_workout(goal, experience_level):

    goal = goal.lower().strip()
    experience_level = experience_level.lower().strip()

    # -----------------------------
    # WEIGHT LOSS
    # -----------------------------
    if goal == "weight loss":

        if experience_level == "beginner":

            return {
                "goal": "Weight Loss",
                "level": "Beginner",
                "workout_duration": "30-40 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Bodyweight Squats - 3 sets x 12 reps",
                        "Wall Push-ups - 3 sets x 10 reps",
                        "Glute Bridges - 3 sets x 12 reps",
                        "Plank - 3 x 20 seconds"
                    ],

                    "Tuesday": [
                        "Brisk Walking - 30 minutes"
                    ],

                    "Wednesday": [
                        "Rest"
                    ],

                    "Thursday": [
                        "Lunges - 3 sets x 10 reps",
                        "Knee Push-ups - 3 sets x 10 reps",
                        "Glute Bridges - 3 sets x 15 reps",
                        "Plank - 3 x 25 seconds"
                    ],

                    "Friday": [
                        "Jumping Jacks - 3 sets x 20 reps",
                        "Bodyweight Squats - 3 sets x 12 reps",
                        "Mountain Climbers - 3 sets x 15 reps"
                    ],

                    "Saturday": [
                        "Walking or Light Jogging - 30 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }

        elif experience_level == "intermediate":

            return {
                "goal": "Weight Loss",
                "level": "Intermediate",
                "workout_duration": "40-50 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Bodyweight Squats - 4 sets x 15 reps",
                        "Push-ups - 3 sets x 12 reps",
                        "Lunges - 3 sets x 12 reps",
                        "Plank - 3 x 40 seconds"
                    ],

                    "Tuesday": [
                        "Jogging - 30 minutes",
                        "Jumping Jacks - 3 sets x 30 reps"
                    ],

                    "Wednesday": [
                        "Rest"
                    ],

                    "Thursday": [
                        "Squats - 4 sets x 15 reps",
                        "Push-ups - 3 sets x 12 reps",
                        "Mountain Climbers - 3 sets x 20 reps",
                        "Plank - 3 x 45 seconds"
                    ],

                    "Friday": [
                        "Lunges - 3 sets x 15 reps",
                        "Jumping Jacks - 4 sets x 25 reps",
                        "Glute Bridges - 4 sets x 15 reps"
                    ],

                    "Saturday": [
                        "Jogging or Cycling - 40 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }

        elif experience_level == "advanced":

            return {
                "goal": "Weight Loss",
                "level": "Advanced",
                "workout_duration": "50-60 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Squats - 4 sets x 20 reps",
                        "Push-ups - 4 sets x 15 reps",
                        "Walking Lunges - 4 sets x 15 reps",
                        "Plank - 4 x 60 seconds"
                    ],

                    "Tuesday": [
                        "Running - 40 minutes",
                        "Mountain Climbers - 4 sets x 25 reps"
                    ],

                    "Wednesday": [
                        "Active Recovery - 30 minutes"
                    ],

                    "Thursday": [
                        "Squats - 4 sets x 20 reps",
                        "Push-ups - 4 sets x 15 reps",
                        "Jumping Jacks - 4 sets x 30 reps",
                        "Mountain Climbers - 4 sets x 25 reps"
                    ],

                    "Friday": [
                        "Lunges - 4 sets x 15 reps",
                        "Glute Bridges - 4 sets x 20 reps",
                        "Plank - 4 x 60 seconds"
                    ],

                    "Saturday": [
                        "Running or Cycling - 45 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }


    # -----------------------------
    # MUSCLE GAIN
    # -----------------------------
    elif goal == "muscle gain":

        if experience_level == "beginner":

            return {
                "goal": "Muscle Gain",
                "level": "Beginner",
                "workout_duration": "30-40 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Bodyweight Squats - 3 sets x 10 reps",
                        "Wall Push-ups - 3 sets x 10 reps",
                        "Glute Bridges - 3 sets x 12 reps"
                    ],

                    "Tuesday": [
                        "Rest"
                    ],

                    "Wednesday": [
                        "Lunges - 3 sets x 10 reps",
                        "Knee Push-ups - 3 sets x 10 reps",
                        "Plank - 3 x 20 seconds"
                    ],

                    "Thursday": [
                        "Rest"
                    ],

                    "Friday": [
                        "Squats - 3 sets x 12 reps",
                        "Push-ups - 3 sets x 8 reps",
                        "Glute Bridges - 3 sets x 15 reps"
                    ],

                    "Saturday": [
                        "Light Walking - 20-30 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }

        elif experience_level == "intermediate":

            return {
                "goal": "Muscle Gain",
                "level": "Intermediate",
                "workout_duration": "40-50 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Squats - 4 sets x 12 reps",
                        "Push-ups - 4 sets x 12 reps",
                        "Lunges - 3 sets x 12 reps",
                        "Glute Bridges - 4 sets x 15 reps"
                    ],

                    "Tuesday": [
                        "Rest or Light Walking - 20 minutes"
                    ],

                    "Wednesday": [
                        "Push-ups - 4 sets x 12 reps",
                        "Squats - 4 sets x 12 reps",
                        "Plank - 3 x 40 seconds"
                    ],

                    "Thursday": [
                        "Rest"
                    ],

                    "Friday": [
                        "Lunges - 4 sets x 12 reps",
                        "Glute Bridges - 4 sets x 20 reps",
                        "Push-ups - 4 sets x 12 reps"
                    ],

                    "Saturday": [
                        "Light Cardio - 30 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }

        elif experience_level == "advanced":

            return {
                "goal": "Muscle Gain",
                "level": "Advanced",
                "workout_duration": "50-60 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Squats - 5 sets x 15 reps",
                        "Push-ups - 5 sets x 15 reps",
                        "Walking Lunges - 4 sets x 15 reps",
                        "Glute Bridges - 4 sets x 20 reps"
                    ],

                    "Tuesday": [
                        "Rest or Light Cardio - 30 minutes"
                    ],

                    "Wednesday": [
                        "Push-ups - 5 sets x 15 reps",
                        "Squats - 5 sets x 15 reps",
                        "Plank - 4 x 60 seconds"
                    ],

                    "Thursday": [
                        "Rest"
                    ],

                    "Friday": [
                        "Lunges - 5 sets x 15 reps",
                        "Glute Bridges - 5 sets x 20 reps",
                        "Push-ups - 5 sets x 15 reps"
                    ],

                    "Saturday": [
                        "Light Cardio - 30 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }


    # -----------------------------
    # GENERAL FITNESS
    # -----------------------------
    elif goal == "general fitness":

        if experience_level == "beginner":

            return {
                "goal": "General Fitness",
                "level": "Beginner",
                "workout_duration": "30-40 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Bodyweight Squats - 3 sets x 12 reps",
                        "Wall Push-ups - 3 sets x 10 reps",
                        "Plank - 3 x 20 seconds"
                    ],

                    "Tuesday": [
                        "Brisk Walking - 25 minutes"
                    ],

                    "Wednesday": [
                        "Rest"
                    ],

                    "Thursday": [
                        "Lunges - 3 sets x 10 reps",
                        "Knee Push-ups - 3 sets x 10 reps",
                        "Glute Bridges - 3 sets x 12 reps"
                    ],

                    "Friday": [
                        "Squats - 3 sets x 12 reps",
                        "Jumping Jacks - 3 sets x 20 reps",
                        "Plank - 3 x 25 seconds"
                    ],

                    "Saturday": [
                        "Walking - 30 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }

        elif experience_level == "intermediate":

            return {
                "goal": "General Fitness",
                "level": "Intermediate",
                "workout_duration": "40-50 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Squats - 4 sets x 15 reps",
                        "Push-ups - 3 sets x 12 reps",
                        "Lunges - 3 sets x 12 reps"
                    ],

                    "Tuesday": [
                        "Jogging - 30 minutes"
                    ],

                    "Wednesday": [
                        "Rest"
                    ],

                    "Thursday": [
                        "Squats - 4 sets x 15 reps",
                        "Push-ups - 3 sets x 12 reps",
                        "Plank - 3 x 40 seconds"
                    ],

                    "Friday": [
                        "Lunges - 3 sets x 15 reps",
                        "Jumping Jacks - 3 sets x 25 reps",
                        "Glute Bridges - 3 sets x 15 reps"
                    ],

                    "Saturday": [
                        "Cycling or Jogging - 30 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }

        elif experience_level == "advanced":

            return {
                "goal": "General Fitness",
                "level": "Advanced",
                "workout_duration": "50-60 minutes",
                "weekly_plan": {

                    "Monday": [
                        "Squats - 4 sets x 20 reps",
                        "Push-ups - 4 sets x 15 reps",
                        "Lunges - 4 sets x 15 reps",
                        "Plank - 4 x 60 seconds"
                    ],

                    "Tuesday": [
                        "Running - 40 minutes"
                    ],

                    "Wednesday": [
                        "Active Recovery - 30 minutes"
                    ],

                    "Thursday": [
                        "Squats - 4 sets x 20 reps",
                        "Push-ups - 4 sets x 15 reps",
                        "Mountain Climbers - 4 sets x 25 reps"
                    ],

                    "Friday": [
                        "Lunges - 4 sets x 15 reps",
                        "Glute Bridges - 4 sets x 20 reps",
                        "Jumping Jacks - 4 sets x 30 reps"
                    ],

                    "Saturday": [
                        "Running or Cycling - 45 minutes"
                    ],

                    "Sunday": [
                        "Rest"
                    ]
                }
            }


    # -----------------------------
    # INVALID COMBINATION
    # -----------------------------
    return {
        "goal": goal,
        "level": experience_level,
        "message": (
            "No personalized workout plan is available. "
            "Use goal: weight loss, muscle gain, or general fitness "
            "and level: beginner, intermediate, or advanced."
        )
    }