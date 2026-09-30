def calculate_bmi(weight, height):
    """
    Calculate BMI.

    weight = kilograms
    height = meters
    """

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return {
        "bmi": round(bmi, 2),
        "category": category
    }