def fitness_chatbot(message):

    message = message.lower().strip()

    if "weight loss" in message or "lose weight" in message:

        return {
            "response": (
                "For weight loss, focus on a balanced diet, "
                "regular exercise, sufficient protein, good sleep "
                "and consistent daily activity."
            )
        }

    elif "muscle" in message or "muscle gain" in message:

        return {
            "response": (
                "For muscle gain, focus on strength training, "
                "adequate protein, enough calories, proper recovery "
                "and consistent sleep."
            )
        }

    elif "squat" in message:

        return {
            "response": (
                "Squats mainly target the legs and glutes. "
                "Keep your back straight, control your movement "
                "and keep your knees aligned with your feet."
            )
        }

    elif "push" in message or "pushup" in message:

        return {
            "response": (
                "Push-ups mainly work the chest, shoulders and triceps. "
                "Keep your body straight and lower yourself with control."
            )
        }

    elif "protein" in message:

        return {
            "response": (
                "Good protein sources include eggs, milk, curd, "
                "paneer, dal, beans, soy, nuts and lean meat."
            )
        }

    elif "workout" in message or "exercise" in message:

        return {
            "response": (
                "For beginners, start with simple exercises such as "
                "squats, push-ups, lunges, glute bridges and planks. "
                "Focus on correct form before increasing intensity."
            )
        }

    else:

        return {
            "response": (
                "I can help with workouts, exercises, weight loss, "
                "muscle gain, protein and basic fitness questions."
            )
        }