EXERCISES = {

    "squat": {
        "name": "Squat",
        "target_muscle": "Quadriceps, Glutes",
        "difficulty": "Beginner",
        "equipment": "None",
        "instructions": [
            "Stand with your feet approximately shoulder-width apart.",
            "Keep your chest upright and your back neutral.",
            "Bend your knees and hips to lower your body.",
            "Push through your feet to return to the starting position."
        ],
        "form_tips": [
            "Keep your knees aligned with your feet.",
            "Keep your heels on the floor.",
            "Avoid rounding your back."
        ]
    },

    "push-up": {
        "name": "Push-up",
        "target_muscle": "Chest, Shoulders, Triceps",
        "difficulty": "Beginner",
        "equipment": "None",
        "instructions": [
            "Start in a plank position with your hands slightly wider than your shoulders.",
            "Keep your body in a straight line.",
            "Lower your chest toward the floor.",
            "Push through your hands to return to the starting position."
        ],
        "form_tips": [
            "Keep your core engaged.",
            "Keep your hips from dropping.",
            "Move in a controlled manner."
        ]
    },

    "lunge": {
        "name": "Lunge",
        "target_muscle": "Quadriceps, Glutes, Hamstrings",
        "difficulty": "Beginner",
        "equipment": "None",
        "instructions": [
            "Stand upright with your feet together.",
            "Step one foot forward.",
            "Lower your body by bending both knees.",
            "Push through the front foot to return to standing."
        ],
        "form_tips": [
            "Keep your upper body upright.",
            "Keep the front knee aligned with the foot.",
            "Use controlled movement."
        ]
    },

    "glute bridge": {
        "name": "Glute Bridge",
        "target_muscle": "Glutes, Hamstrings",
        "difficulty": "Beginner",
        "equipment": "None",
        "instructions": [
            "Lie on your back with your knees bent.",
            "Place your feet flat on the floor.",
            "Lift your hips upward.",
            "Lower your hips slowly."
        ],
        "form_tips": [
            "Keep your feet stable.",
            "Avoid excessive arching of your lower back.",
            "Squeeze your glutes at the top."
        ]
    },

    "plank": {
        "name": "Plank",
        "target_muscle": "Core",
        "difficulty": "Beginner",
        "equipment": "None",
        "instructions": [
            "Place your forearms on the floor.",
            "Extend your legs behind you.",
            "Keep your body in a straight line.",
            "Hold the position while maintaining controlled breathing."
        ],
        "form_tips": [
            "Keep your hips level.",
            "Keep your core engaged.",
            "Avoid holding your breath."
        ]
    }
}


def get_exercise(exercise_name):

    exercise_name = exercise_name.lower().strip()

    return EXERCISES.get(exercise_name)