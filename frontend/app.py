import streamlit as st
import requests


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Gym & Fitness Assistant",
    page_icon="🏋️",
    layout="wide"
)


# --------------------------------------------------
# BACKEND URL
# --------------------------------------------------

BACKEND_URL = "http://127.0.0.1:8000"


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏋️ AI Gym & Fitness Assistant")

st.write(
    "Your AI-powered fitness dashboard for workout, "
    "nutrition, BMI, chatbot and progress tracking."
)

st.divider()


# --------------------------------------------------
# SIDEBAR - USER PROFILE
# --------------------------------------------------

st.sidebar.header("👤 User Profile")

name = st.sidebar.text_input(
    "Name",
    value="Spoorthi"
)

age = st.sidebar.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=22
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

height = st.sidebar.number_input(
    "Height (meters)",
    min_value=1.0,
    max_value=2.5,
    value=1.60,
    step=0.01
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=55.0,
    step=0.1
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "weight loss",
        "muscle gain",
        "general fitness"
    ]
)

experience_level = st.sidebar.selectbox(
    "Experience Level",
    [
        "beginner",
        "intermediate",
        "advanced"
    ]
)

activity_level = st.sidebar.selectbox(
    "Activity Level",
    [
        "sedentary",
        "light",
        "moderate",
        "active"
    ]
)


# --------------------------------------------------
# DIETARY PREFERENCE
# --------------------------------------------------

dietary_preference = st.sidebar.selectbox(
    "Dietary Preference",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan"
    ]
)


# --------------------------------------------------
# BUTTON
# --------------------------------------------------

generate_button = st.sidebar.button(
    "Generate Fitness Plan"
)


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if generate_button:

    # ----------------------------------------------
    # BMI
    # ----------------------------------------------

    try:

        bmi_response = requests.get(
            f"{BACKEND_URL}/fitness/bmi",
            params={
                "weight": weight,
                "height": height
            }
        )

        bmi_data = bmi_response.json()

    except Exception:

        bmi_data = None


    # ----------------------------------------------
    # WORKOUT
    # ----------------------------------------------

    try:

        workout_response = requests.get(
            f"{BACKEND_URL}/workout/recommendation",
            params={
                "goal": goal,
                "experience_level": experience_level
            }
        )

        workout_data = workout_response.json()

    except Exception:

        workout_data = None


    # ----------------------------------------------
    # NUTRITION
    # ----------------------------------------------

    try:

        nutrition_response = requests.get(
            f"{BACKEND_URL}/nutrition/recommendation",
            params={
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight,
                "activity_level": activity_level,
                "goal": goal,
                "dietary_preference": dietary_preference
            }
        )

        nutrition_data = nutrition_response.json()

    except Exception:

        nutrition_data = None


    # ----------------------------------------------
    # DISPLAY USER
    # ----------------------------------------------

    st.subheader(f"Welcome, {name}! 👋")

    st.write(
        f"Goal: **{goal.title()}**  |  "
        f"Experience: **{experience_level.title()}**  |  "
        f"Diet: **{dietary_preference}**"
    )

    st.divider()


    # ----------------------------------------------
    # FITNESS SUMMARY
    # ----------------------------------------------

    st.subheader("📊 Fitness Summary")

    col1, col2, col3 = st.columns(3)


    # BMI

    with col1:

        st.metric(
            "BMI",
            bmi_data["bmi"] if bmi_data else "N/A"
        )

        if bmi_data:

            st.write(
                f"Category: **{bmi_data['category']}**"
            )


    # Calories

    with col2:

        if nutrition_data:

            calories = nutrition_data[
                "nutrition_targets"
            ][
                "estimated_daily_calories"
            ]

            st.metric(
                "Daily Calories",
                f"{calories} kcal"
            )

        else:

            st.metric(
                "Daily Calories",
                "N/A"
            )


    # Protein

    with col3:

        if nutrition_data:

            protein = nutrition_data[
                "nutrition_targets"
            ][
                "protein_grams_per_day"
            ]

            st.metric(
                "Protein",
                f"{protein} g"
            )

        else:

            st.metric(
                "Protein",
                "N/A"
            )


    st.divider()


    # ----------------------------------------------
    # WORKOUT PLAN
    # ----------------------------------------------

    st.subheader("🏋️ Recommended Workout")

    if workout_data:

        if "weekly_plan" in workout_data:

            st.write(
                f"**Duration:** "
                f"{workout_data.get('workout_duration', 'N/A')}"
            )

            weekly_plan = workout_data["weekly_plan"]

            for day, exercises in weekly_plan.items():

                st.markdown(f"### {day}")

                for exercise in exercises:

                    st.write(f"• {exercise}")

        else:

            st.info(
                workout_data.get(
                    "message",
                    "No workout plan available."
                )
            )

    else:

        st.error(
            "Could not connect to workout service."
        )


    st.divider()


    # ----------------------------------------------
    # NUTRITION PLAN
    # ----------------------------------------------

    st.subheader("🥗 Nutrition Plan")

    if nutrition_data:

        # Dietary Preference

        st.write(
            f"**Dietary Preference:** "
            f"{nutrition_data.get(
                'dietary_preference',
                dietary_preference
            )}"
        )


        # Meal Plan

        st.write("### 🍽️ Personalized Meal Plan")

        meal_plan = nutrition_data["meal_plan"]

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**🌅 Breakfast:** "
                f"{meal_plan['breakfast']}"
            )

            st.write(
                f"**🍎 Mid-morning:** "
                f"{meal_plan['mid_morning']}"
            )

            st.write(
                f"**🍛 Lunch:** "
                f"{meal_plan['lunch']}"
            )

        with col2:

            st.write(
                f"**☕ Evening Snack:** "
                f"{meal_plan['evening_snack']}"
            )

            st.write(
                f"**🌙 Dinner:** "
                f"{meal_plan['dinner']}"
            )


        # Grocery List

        st.write("### 🛒 Grocery List")

        grocery_list = nutrition_data.get(
            "grocery_list",
            []
        )

        if grocery_list:

            for item in grocery_list:

                st.write(
                    f"☐ {item}"
                )

        else:

            st.info(
                "No grocery list available."
            )


        # Nutrition Note

        st.info(
            nutrition_data.get(
                "note",
                ""
            )
        )

    else:

        st.error(
            "Could not connect to nutrition service."
        )


    st.divider()


    # ----------------------------------------------
    # CHATBOT
    # ----------------------------------------------

    st.subheader("🤖 Fitness Chatbot")

    question = st.text_input(
        "Ask your fitness question"
    )

    if question:

        try:

            chatbot_response = requests.get(
                f"{BACKEND_URL}/chatbot/ask",
                params={
                    "message": question
                }
            )

            chatbot_data = chatbot_response.json()

            st.success(
                chatbot_data["response"]
            )

        except Exception:

            st.error(
                "Could not connect to chatbot."
            )


else:

    # ----------------------------------------------
    # INITIAL SCREEN
    # ----------------------------------------------

    st.info(
        "👈 Enter your profile information "
        "and click **Generate Fitness Plan** "
        "to start."
    )


# --------------------------------------------------
# CHATBOT
# --------------------------------------------------

if not generate_button:

    st.subheader("🤖 Fitness Chatbot")

    question = st.text_input(
        "Ask your fitness question",
        key="initial_chatbot"
    )

    if question:

        try:

            chatbot_response = requests.get(
                f"{BACKEND_URL}/chatbot/ask",
                params={
                    "message": question
                }
            )

            chatbot_data = chatbot_response.json()

            st.success(
                chatbot_data["response"]
            )

        except Exception:

            st.error(
                "Could not connect to chatbot."
            )

            # --------------------------------------------------
# AI MOOD & SENTIMENT ANALYSIS
# --------------------------------------------------

st.divider()

st.subheader("🧠 AI Mood & Sentiment Analysis")

st.write(
    "Tell the AI how you are feeling and get "
    "personalized fitness and motivational guidance."
)

mood_message = st.text_input(
    "How are you feeling today?",
    placeholder="Example: I am feeling tired and unmotivated today",
    key="mood_message"
)

if st.button("🔍 Analyze My Mood"):

    if mood_message.strip():

        try:

            mood_response = requests.get(
                f"{BACKEND_URL}/mood/analyze",
                params={
                    "message": mood_message
                },
                timeout=10
            )

            if mood_response.status_code == 200:

                mood_data = mood_response.json()

                # ----------------------------------
                # MOOD
                # ----------------------------------

                st.write(
                    f"### 💭 Mood: "
                    f"**{mood_data.get('mood', 'N/A')}**"
                )

                # ----------------------------------
                # SENTIMENT
                # ----------------------------------

                st.write(
                    f"**Sentiment:** "
                    f"{mood_data.get('sentiment', 'N/A')}"
                )

                # ----------------------------------
                # SCORES
                # ----------------------------------

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Positive Score",
                        mood_data.get(
                            "positive_score",
                            0
                        )
                    )

                with col2:

                    st.metric(
                        "Negative Score",
                        mood_data.get(
                            "negative_score",
                            0
                        )
                    )

                # ----------------------------------
                # ADVICE
                # ----------------------------------

                st.write(
                    "### 💡 AI Advice"
                )

                st.info(
                    mood_data.get(
                        "advice",
                        "No advice available."
                    )
                )

                # ----------------------------------
                # FITNESS RECOMMENDATION
                # ----------------------------------

                st.write(
                    "### 🏋️ Fitness Recommendation"
                )

                st.write(
                    mood_data.get(
                        "fitness_recommendation",
                        "No fitness recommendation available."
                    )
                )

                # ----------------------------------
                # MOTIVATION
                # ----------------------------------

                st.write(
                    "### 🌟 Motivation"
                )

                st.success(
                    mood_data.get(
                        "motivation",
                        "Keep moving forward! 💪"
                    )
                )

            else:

                st.error(
                    "Mood analysis service returned an error."
                )

        except Exception as e:

            st.error(
                f"Could not connect to mood analysis: {e}"
            )

    else:

        st.warning(
            "Please describe how you are feeling first."
        )


# --------------------------------------------------
# PROGRESS TRACKING
# --------------------------------------------------

st.divider()

st.subheader("📈 Workout Progress")

try:

    progress_response = requests.get(
        f"{BACKEND_URL}/progress/summary"
    )

    progress_data = progress_response.json()

    progress = progress_data["progress"]

    # Performance Score

    performance_score = progress.get(
        "performance_score",
        0
    )

    st.metric(
        "🏆 Performance Score",
        f"{performance_score}%"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Workouts",
            progress["total_workouts"]
        )

    with col2:

        st.metric(
            "Completed Reps",
            progress["total_completed_reps"]
        )

    with col3:

        st.metric(
            "Workout Time",
            f"{progress['total_workout_duration_minutes']} min"
        )

    with col4:

        st.metric(
            "Average Reps",
            progress["average_reps_per_workout"]
        )

    st.write("### Exercise Statistics")

    exercise_statistics = progress[
        "exercise_statistics"
    ]

    for exercise, statistics in exercise_statistics.items():

        st.write(f"**{exercise}**")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"Workouts: "
                f"{statistics['workouts']}"
            )

        with col2:

            st.write(
                f"Total Reps: "
                f"{statistics['total_reps']}"
            )

        with col3:

            st.write(
                f"Duration: "
                f"{round(statistics['total_duration_minutes'], 2)} min"
            )

except Exception:

    st.error(
        "Could not connect to progress tracking."
    )


# --------------------------------------------------
# AI EXERCISE DETECTION
# --------------------------------------------------

st.divider()

st.subheader("📷 AI Exercise Detection")

st.write(
    "Use your camera to automatically count "
    "exercise repetitions using AI pose detection."
)

col1, col2 = st.columns(2)

with col1:

    if st.button("🦵 Start Squat Detection"):

        st.info(
            "Camera is starting. Perform your squats "
            "and press Q to finish."
        )

        try:

            squat_response = requests.get(
                f"{BACKEND_URL}/exercise/start/squat",
                timeout=600
            )

            if squat_response.status_code == 200:

                squat_data = squat_response.json()

                st.success(
                    "Squat workout completed!"
                )

                result = squat_data[
                    "workout_result"
                ]

                st.write(
                    f"**Exercise:** "
                    f"{result['exercise']}"
                )

                st.write(
                    f"**Target Reps:** "
                    f"{result['target_reps']}"
                )

                st.write(
                    f"**Completed Reps:** "
                    f"{result['completed_reps']}"
                )

                st.write(
                    f"**Form Feedback:** "
                    f"{result['form_feedback']}"
                )

                st.write(
                    f"**Duration:** "
                    f"{result['duration_minutes']} minutes"
                )

            else:

                st.error(
                    "Squat detection failed."
                )

        except Exception as e:

            st.error(
                f"Could not start squat detection: {e}"
            )


with col2:

    if st.button("💪 Start Push-up Detection"):

        st.info(
            "Camera is starting. Perform your push-ups "
            "and press Q to finish."
        )

        try:

            pushup_response = requests.get(
                f"{BACKEND_URL}/exercise/start/pushup",
                timeout=600
            )

            if pushup_response.status_code == 200:

                pushup_data = pushup_response.json()

                st.success(
                    "Push-up workout completed!"
                )

                result = pushup_data[
                    "workout_result"
                ]

                st.write(
                    f"**Exercise:** "
                    f"{result['exercise']}"
                )

                st.write(
                    f"**Target Reps:** "
                    f"{result['target_reps']}"
                )

                st.write(
                    f"**Completed Reps:** "
                    f"{result['completed_reps']}"
                )

                st.write(
                    f"**Form Feedback:** "
                    f"{result['form_feedback']}"
                )

                st.write(
                    f"**Duration:** "
                    f"{result['duration_minutes']} minutes"
                )

            else:

                st.error(
                    "Push-up detection failed."
                )

        except Exception as e:

            st.error(
                f"Could not start push-up detection: {e}"
            )

            # --------------------------------------------------
# FITNESS HABIT TRACKER
# --------------------------------------------------

st.divider()

st.subheader("📅 Fitness Habit Tracker")

st.write(
    "Analyze your workout consistency, current streak, "
    "workout frequency and fitness behavior."
)

try:

    habit_response = requests.get(
        f"{BACKEND_URL}/habit/summary",
        timeout=10
    )

    if habit_response.status_code == 200:

        habit_data = habit_response.json()

        habit = habit_data.get(
            "habit_analysis",
            {}
        )

        # ------------------------------------------
        # HABIT STATUS
        # ------------------------------------------

        st.write(
            f"### 🔥 Habit Status: "
            f"**{habit.get('habit_status', 'N/A')}**"
        )

        # ------------------------------------------
        # HABIT METRICS
        # ------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Workout Days",
                habit.get(
                    "workout_days",
                    0
                )
            )

        with col2:

            st.metric(
                "Current Streak",
                f"{habit.get('current_streak', 0)} days"
            )

        with col3:

            st.metric(
                "Workout Frequency",
                habit.get(
                    "workout_frequency",
                    0
                )
            )

        with col4:

            st.metric(
                "Consistency",
                f"{habit.get('consistency_percentage', 0)}%"
            )

        # ------------------------------------------
        # TOTAL WORKOUTS
        # ------------------------------------------

        st.write(
            f"**Total Recorded Workouts:** "
            f"{habit.get('total_workouts', 0)}"
        )

        # ------------------------------------------
        # BEHAVIOR ANALYSIS
        # ------------------------------------------

        st.write("### 🧠 Behavior Analysis")

        st.info(
            habit.get(
                "behavior_analysis",
                "No behavior analysis available."
            )
        )

        # ------------------------------------------
        # RECOMMENDATION
        # ------------------------------------------

        st.write("### 💡 Personalized Recommendation")

        st.write(
            habit.get(
                "recommendation",
                "No recommendation available."
            )
        )

        # ------------------------------------------
        # MOTIVATIONAL NUDGE
        # ------------------------------------------

        st.write("### 🌟 Motivational Nudge")

        st.success(
            habit.get(
                "motivational_nudge",
                "Keep going! 💪"
            )
        )

    else:

        st.error(
            "Habit tracker service returned an error."
        )

except Exception as e:

    st.error(
        f"Could not connect to habit tracker: {e}"
    )

    # --------------------------------------------------
# SMART GYM ASSISTANT
# --------------------------------------------------

st.divider()

st.subheader("⚙️ Smart Gym Assistant")

st.write(
    "Monitor gym equipment and receive AI-based "
    "workout intensity, resistance and rest recommendations."
)

col1, col2 = st.columns(2)

with col1:

    smart_equipment = st.selectbox(
        "Select Equipment",
        [
            "Treadmill",
            "Exercise Bike",
            "Cross Trainer",
            "Leg Press"
        ],
        key="smart_equipment"
    )

with col2:

    smart_intensity = st.selectbox(
        "Workout Intensity",
        [
            "Low",
            "Moderate",
            "High"
        ],
        key="smart_intensity"
    )


if st.button("⚙️ Check Smart Gym Status"):

    try:

        smart_response = requests.get(
            f"{BACKEND_URL}/smart-gym/status",
            params={
                "equipment": smart_equipment,
                "intensity": smart_intensity
            },
            timeout=10
        )

        if smart_response.status_code == 200:

            smart_data = smart_response.json()

            # ------------------------------------------
            # EQUIPMENT STATUS
            # ------------------------------------------

            st.write(
                f"### 🏋️ {smart_data.get('equipment', 'N/A')}"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Equipment Status",
                    smart_data.get(
                        "equipment_status",
                        "N/A"
                    )
                )

            with col2:

                st.metric(
                    "Temperature",
                    f"{smart_data.get('simulated_temperature_c', 0)} °C"
                )

            with col3:

                st.metric(
                    "Heart Rate",
                    f"{smart_data.get('simulated_heart_rate_bpm', 0)} BPM"
                )

            with col4:

                st.metric(
                    "Resistance",
                    smart_data.get(
                        "current_resistance",
                        0
                    )
                )

            # ------------------------------------------
            # AI RECOMMENDATIONS
            # ------------------------------------------

            st.write("### 🤖 AI Workout Recommendation")

            st.write(
                f"**Current Intensity:** "
                f"{smart_data.get('workout_intensity', 'N/A')}"
            )

            st.write(
                f"**Recommended Intensity:** "
                f"{smart_data.get('recommended_intensity', 'N/A')}"
            )

            st.write(
                f"**Resistance Adjustment:** "
                f"{smart_data.get('resistance_adjustment', 'N/A')}"
            )

            st.write(
                f"**Rest Recommendation:** "
                f"{smart_data.get('rest_recommendation', 'N/A')}"
            )

            # ------------------------------------------
            # SAFETY STATUS
            # ------------------------------------------

            st.write("### 🛡️ Equipment Safety")

            if smart_data.get("safety_status") == "Normal":

                st.success(
                    "Equipment Status: Normal ✅"
                )

            else:

                st.warning(
                    smart_data.get(
                        "safety_status",
                        "Check equipment."
                    )
                )

            # ------------------------------------------
            # IOT MODE
            # ------------------------------------------

            st.info(
                f"📡 IoT Mode: "
                f"{smart_data.get('iot_mode', 'Simulation')}"
            )

        else:

            st.error(
                "Smart Gym service returned an error."
            )

    except Exception as e:

        st.error(
            f"Could not connect to Smart Gym service: {e}"
        )

        # --------------------------------------------------
# WEEKLY PERFORMANCE REPORT
# --------------------------------------------------

st.divider()

st.subheader("📊 Weekly Performance Report")

st.write(
    "View your weekly workout performance, "
    "consistency, exercise statistics and "
    "personalized improvement recommendations."
)

try:

    weekly_report_response = requests.get(
        f"{BACKEND_URL}/report/weekly",
        timeout=10
    )

    if weekly_report_response.status_code == 200:

        weekly_report_data = weekly_report_response.json()

        weekly_report = weekly_report_data.get(
            "weekly_report",
            {}
        )

        # ------------------------------------------
        # REPORT PERIOD
        # ------------------------------------------

        st.write(
            f"### 📅 Report Period: "
            f"**{weekly_report.get('report_period', 'N/A')}**"
        )

        # ------------------------------------------
        # REPORT STATUS
        # ------------------------------------------

        report_status = weekly_report.get(
            "report_status",
            "Report generated"
        )

        if report_status == "Report generated":

            st.success(
                "Weekly report generated successfully! ✅"
            )

        else:

            st.info(
                "ℹ️ "
                + weekly_report.get(
                    "summary",
                    "No weekly workout data available yet."
                )
            )

        # ------------------------------------------
        # WEEKLY METRICS
        # ------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Weekly Workouts",
                weekly_report.get(
                    "weekly_workouts",
                    0
                )
            )

        with col2:

            st.metric(
                "Workout Days",
                weekly_report.get(
                    "workout_days",
                    0
                )
            )

        with col3:

            st.metric(
                "Total Reps",
                weekly_report.get(
                    "total_reps",
                    0
                )
            )

        with col4:

            st.metric(
                "Performance Score",
                f"{weekly_report.get('performance_score', 0)}%"
            )

        # ------------------------------------------
        # ADDITIONAL METRICS
        # ------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Workout Duration",
                f"{weekly_report.get('total_duration_minutes', 0)} min"
            )

        with col2:

            st.metric(
                "Weekly Consistency",
                f"{weekly_report.get('consistency_percentage', 0)}%"
            )

        # ------------------------------------------
        # EXERCISE STATISTICS
        # ------------------------------------------

        exercise_statistics = weekly_report.get(
            "exercise_statistics",
            {}
        )

        if exercise_statistics:

            st.write("### 🏋️ Exercise-wise Weekly Performance")

            for exercise, statistics in exercise_statistics.items():

                st.write(
                    f"**{exercise}**"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.write(
                        f"Workouts: "
                        f"{statistics.get('workouts', 0)}"
                    )

                with col2:

                    st.write(
                        f"Total Reps: "
                        f"{statistics.get('total_reps', 0)}"
                    )

                with col3:

                    st.write(
                        f"Duration: "
                        f"{statistics.get('total_duration_minutes', 0)} min"
                    )

        # ------------------------------------------
        # WEEKLY SUMMARY
        # ------------------------------------------

        st.write("### 📝 Weekly Summary")

        st.info(
            weekly_report.get(
                "summary",
                "No weekly summary available."
            )
        )

        # ------------------------------------------
        # IMPROVEMENT RECOMMENDATION
        # ------------------------------------------

        st.write(
            "### 💡 Personalized Improvement Recommendation"
        )

        st.success(
            weekly_report.get(
                "improvement_recommendation",
                "Continue your fitness routine."
            )
        )

    else:

        st.error(
            "Weekly performance report service "
            "returned an error."
        )

except Exception as e:

    st.error(
        f"Could not connect to weekly performance report: {e}"
    )


# --------------------------------------------------
# FEATURES
# --------------------------------------------------

st.markdown(
    """
    ### Features

    🧮 **BMI Calculation**

    🏋️ **AI Workout Recommendation**

    🥗 **Personalized Nutrition Recommendation**

    🛒 **Dietary Preference & Grocery List**

    🤖 **Fitness Chatbot**

    📈 **Workout Progress Tracking**

    🏆 **Performance Score**

    📅 **Fitness Habit Tracker**

    ⚙️ **Smart Gym Assistant / IoT Simulation**

    📷 **AI Exercise Detection**
    """
)