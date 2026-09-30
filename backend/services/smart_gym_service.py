# --------------------------------------------------
# SMART GYM ASSISTANT SERVICE
# Simulated IoT Equipment Monitoring
# --------------------------------------------------


def get_equipment_status(
    equipment="Treadmill",
    intensity="Moderate"
):

    equipment = equipment.strip().title()
    intensity = intensity.strip().lower()


    # --------------------------------------------------
    # SIMULATED SENSOR VALUES
    # --------------------------------------------------

    sensor_data = {

        "Treadmill": {
            "temperature": 32,
            "usage_status": "In Use",
            "current_resistance": 5
        },

        "Exercise Bike": {
            "temperature": 30,
            "usage_status": "Available",
            "current_resistance": 4
        },

        "Cross Trainer": {
            "temperature": 31,
            "usage_status": "Available",
            "current_resistance": 6
        },

        "Leg Press": {
            "temperature": 29,
            "usage_status": "Available",
            "current_resistance": 40
        }
    }


    equipment_data = sensor_data.get(
        equipment,
        {
            "temperature": 30,
            "usage_status": "Available",
            "current_resistance": 5
        }
    )


    # --------------------------------------------------
    # SIMULATED HEART RATE
    # --------------------------------------------------

    heart_rates = {
        "low": 90,
        "moderate": 120,
        "high": 150
    }

    heart_rate = heart_rates.get(
        intensity,
        120
    )


    # --------------------------------------------------
    # AI INTENSITY RECOMMENDATION
    # --------------------------------------------------

    if intensity == "low":

        recommended_intensity = "Moderate"

        resistance_adjustment = "Increase slightly"

        rest_recommendation = (
            "Take a short 30-60 second rest "
            "between exercise sets."
        )

    elif intensity == "moderate":

        recommended_intensity = "Moderate"

        resistance_adjustment = "Maintain current level"

        rest_recommendation = (
            "Take approximately 60 seconds of rest "
            "between exercise sets."
        )

    else:

        recommended_intensity = "Low to Moderate"

        resistance_adjustment = "Reduce slightly"

        rest_recommendation = (
            "Take 1-2 minutes of rest and allow "
            "your heart rate to recover."
        )


    # --------------------------------------------------
    # EQUIPMENT SAFETY STATUS
    # --------------------------------------------------

    if equipment_data["temperature"] > 35:

        safety_status = "Warning - Equipment temperature is high"

    else:

        safety_status = "Normal"


    # --------------------------------------------------
    # RETURN SMART GYM DATA
    # --------------------------------------------------

    return {

        "equipment": equipment,

        "equipment_status": equipment_data[
            "usage_status"
        ],

        "simulated_temperature_c": equipment_data[
            "temperature"
        ],

        "current_resistance": equipment_data[
            "current_resistance"
        ],

        "simulated_heart_rate_bpm": heart_rate,

        "workout_intensity": intensity.title(),

        "recommended_intensity": recommended_intensity,

        "resistance_adjustment": resistance_adjustment,

        "rest_recommendation": rest_recommendation,

        "safety_status": safety_status,

        "iot_mode": "Simulation",

        "message": (
            "Smart gym equipment monitoring and "
            "AI-based workout adjustment completed."
        )
    }