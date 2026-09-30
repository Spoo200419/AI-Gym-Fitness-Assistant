# --------------------------------------------------
# AI MOOD & SENTIMENT ANALYSIS SERVICE
# --------------------------------------------------


POSITIVE_WORDS = [
    "happy",
    "good",
    "great",
    "excellent",
    "motivated",
    "energetic",
    "strong",
    "excited",
    "confident",
    "fresh",
    "amazing",
    "positive",
    "better",
    "healthy"
]


NEGATIVE_WORDS = [
    "sad",
    "bad",
    "tired",
    "weak",
    "lazy",
    "unmotivated",
    "stressed",
    "stress",
    "angry",
    "upset",
    "bored",
    "worried",
    "anxious",
    "exhausted",
    "depressed",
    "frustrated",
    "pain"
]


def analyze_mood(message):

    message = message.lower().strip()

    positive_score = 0
    negative_score = 0

    # ----------------------------------------------
    # SENTIMENT SCORING
    # ----------------------------------------------

    words = message.split()

    for word in words:

        clean_word = word.strip(
            ".,!?;:"
        )

        if clean_word in POSITIVE_WORDS:
            positive_score += 1

        if clean_word in NEGATIVE_WORDS:
            negative_score += 1


    # ----------------------------------------------
    # DETERMINE MOOD
    # ----------------------------------------------

    if positive_score > negative_score:

        mood = "Positive"
        sentiment = "Positive"

        advice = (
            "You seem to be feeling positive and motivated. "
            "Use this energy to complete your workout and "
            "maintain your fitness routine."
        )

        fitness_recommendation = (
            "Try a normal workout session and gradually "
            "increase the intensity if you feel comfortable."
        )


    elif negative_score > positive_score:

        mood = "Low / Tired"
        sentiment = "Negative"

        advice = (
            "It sounds like you may be feeling tired or "
            "unmotivated. Take a short break, stay hydrated "
            "and listen to your body."
        )

        fitness_recommendation = (
            "Consider a light workout such as walking, "
            "stretching or mobility exercises."
        )


    else:

        mood = "Neutral"
        sentiment = "Neutral"

        advice = (
            "Your message shows a neutral mood. "
            "A simple workout or short walk can help "
            "maintain your energy and routine."
        )

        fitness_recommendation = (
            "Try a moderate workout based on your "
            "current energy level."
        )


    # ----------------------------------------------
    # MOTIVATIONAL MESSAGE
    # ----------------------------------------------

    if sentiment == "Positive":

        motivation = (
            "Keep the positive energy going! "
            "Every workout brings you closer to your goal. 💪🔥"
        )

    elif sentiment == "Negative":

        motivation = (
            "You don't have to be perfect every day. "
            "Start small and keep moving forward. 🌱💪"
        )

    else:

        motivation = (
            "Consistency matters more than motivation. "
            "Take one small step toward your fitness goal today. 🌟"
        )


    # ----------------------------------------------
    # RETURN ANALYSIS
    # ----------------------------------------------

    return {

        "message": message,

        "mood": mood,

        "sentiment": sentiment,

        "positive_score": positive_score,

        "negative_score": negative_score,

        "advice": advice,

        "fitness_recommendation": fitness_recommendation,

        "motivation": motivation
    }