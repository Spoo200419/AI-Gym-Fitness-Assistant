def calculate_daily_calories(
    age,
    gender,
    height,
    weight,
    activity_level,
    goal
):
    """
    Estimate daily calorie needs using the
    Mifflin-St Jeor equation and an activity factor.
    """

    gender = gender.lower().strip()
    activity_level = activity_level.lower().strip()
    goal = goal.lower().strip()

    # Calculate Basal Metabolic Rate (BMR)
    height_cm = height * 100

    if gender == "male":

        bmr = (
            10 * weight
            + 6.25 * height_cm
            - 5 * age
            + 5
        )

    else:

        bmr = (
            10 * weight
            + 6.25 * height_cm
            - 5 * age
            - 161
        )

    # Activity multiplier
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }

    activity_factor = activity_factors.get(
        activity_level,
        1.2
    )

    maintenance_calories = bmr * activity_factor

    # Adjust calories according to fitness goal
    if "weight loss" in goal:

        daily_calories = maintenance_calories - 400

    elif "muscle gain" in goal:

        daily_calories = maintenance_calories + 300

    else:

        daily_calories = maintenance_calories

    # Protein recommendation
    if "muscle gain" in goal:

        protein_per_kg = 1.6

    elif "weight loss" in goal:

        protein_per_kg = 1.4

    else:

        protein_per_kg = 1.2

    protein_grams = weight * protein_per_kg

    return {
        "estimated_daily_calories": round(
            daily_calories
        ),
        "estimated_maintenance_calories": round(
            maintenance_calories
        ),
        "protein_grams_per_day": round(
            protein_grams
        ),
        "protein_target_per_kg": protein_per_kg
    }


# --------------------------------------------------
# MEAL PLAN
# --------------------------------------------------

def generate_meal_plan(
    goal,
    dietary_preference="vegetarian"
):

    goal = goal.lower().strip()
    dietary_preference = (
        dietary_preference.lower().strip()
    )

    # VEGAN MEAL PLANS
    if dietary_preference == "vegan":

        if "weight loss" in goal:

            return {
                "breakfast": "Oats with soy milk, banana and chia seeds",
                "mid_morning": "Apple or orange",
                "lunch": "2 chapatis, dal, mixed vegetables and salad",
                "evening_snack": "Roasted chana or sprouts",
                "dinner": "Vegetable soup, tofu and salad"
            }

        elif "muscle gain" in goal:

            return {
                "breakfast": "Oats with soy milk, banana, peanut butter and chia seeds",
                "mid_morning": "Fruit with mixed nuts",
                "lunch": "Rice or chapatis, dal, vegetables and tofu",
                "evening_snack": "Soy milk smoothie with banana and nuts",
                "dinner": "Chapatis with vegetables, beans and tofu"
            }

        else:

            return {
                "breakfast": "Oats with soy milk and fruit",
                "mid_morning": "Seasonal fruit",
                "lunch": "Rice or chapatis with dal, vegetables and salad",
                "evening_snack": "Roasted chana or sprouts",
                "dinner": "Chapatis with vegetables and dal"
            }

    # NON-VEGETARIAN MEAL PLANS
    elif dietary_preference in [
        "non-vegetarian",
        "non vegetarian",
        "nonveg",
        "non-veg"
    ]:

        if "weight loss" in goal:

            return {
                "breakfast": "Oats with milk, banana and boiled eggs",
                "mid_morning": "Apple or orange",
                "lunch": "2 chapatis, dal, vegetables, curd and grilled chicken",
                "evening_snack": "Roasted chana or boiled eggs",
                "dinner": "Vegetable soup, grilled chicken/fish and salad"
            }

        elif "muscle gain" in goal:

            return {
                "breakfast": "Oats, milk, banana, eggs and peanut butter",
                "mid_morning": "Fruit with nuts",
                "lunch": "Rice or chapatis, dal, vegetables, curd and chicken",
                "evening_snack": "Milk or curd with banana and nuts",
                "dinner": "Rice/chapatis, vegetables and chicken/fish"
            }

        else:

            return {
                "breakfast": "Oats, milk, fruit and eggs",
                "mid_morning": "Seasonal fruit",
                "lunch": "Rice or chapatis with dal, vegetables, curd and chicken",
                "evening_snack": "Fruit or boiled eggs",
                "dinner": "Chapatis with vegetables and fish/chicken"
            }

    # VEGETARIAN MEAL PLANS
    else:

        if "weight loss" in goal:

            return {
                "breakfast": "Oats with milk, banana and a few nuts",
                "mid_morning": "One fruit such as apple or orange",
                "lunch": "2 chapatis, dal, mixed vegetables and curd",
                "evening_snack": "Roasted chana or sprouts",
                "dinner": "Vegetable soup, paneer/tofu and salad"
            }

        elif "muscle gain" in goal:

            return {
                "breakfast": "Oats, milk, banana, eggs or paneer",
                "mid_morning": "Fruit with nuts",
                "lunch": "Rice or chapatis, dal, vegetables and paneer",
                "evening_snack": "Milk or curd with banana and nuts",
                "dinner": "Chapatis/rice with vegetables and paneer/tofu"
            }

        else:

            return {
                "breakfast": "Oats or idli with fruit",
                "mid_morning": "Seasonal fruit",
                "lunch": "Rice or chapatis with dal, vegetables and curd",
                "evening_snack": "Fruit or roasted chana",
                "dinner": "Chapatis with vegetables and dal"
            }


# --------------------------------------------------
# GROCERY LIST
# --------------------------------------------------

def generate_grocery_list(
    goal,
    dietary_preference="vegetarian"
):

    goal = goal.lower().strip()
    dietary_preference = (
        dietary_preference.lower().strip()
    )

    # Common groceries
    groceries = [
        "Oats",
        "Bananas",
        "Apples",
        "Seasonal fruits",
        "Mixed vegetables",
        "Leafy vegetables",
        "Tomatoes",
        "Onions",
        "Chapati/Roti flour",
        "Rice",
        "Dal",
        "Roasted chana",
        "Sprouts",
        "Nuts",
        "Chia seeds",
        "Salad vegetables"
    ]

    # Vegan groceries
    if dietary_preference == "vegan":

        groceries.extend([
            "Soy milk",
            "Tofu",
            "Beans",
            "Peanut butter"
        ])

    # Non-vegetarian groceries
    elif dietary_preference in [
        "non-vegetarian",
        "non vegetarian",
        "nonveg",
        "non-veg"
    ]:

        groceries.extend([
            "Eggs",
            "Chicken",
            "Fish",
            "Milk",
            "Curd"
        ])

    # Vegetarian groceries
    else:

        groceries.extend([
            "Milk",
            "Curd",
            "Paneer",
            "Tofu"
        ])

    # Extra protein foods for muscle gain
    if "muscle gain" in goal:

        groceries.extend([
            "Peanut butter",
            "Protein-rich beans",
            "Extra paneer/tofu"
        ])

    return groceries


# --------------------------------------------------
# COMPLETE NUTRITION PLAN
# --------------------------------------------------

def generate_nutrition_plan(
    age,
    gender,
    height,
    weight,
    activity_level,
    goal,
    dietary_preference="vegetarian"
):

    nutrition = calculate_daily_calories(
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        activity_level=activity_level,
        goal=goal
    )

    meals = generate_meal_plan(
        goal=goal,
        dietary_preference=dietary_preference
    )

    grocery_list = generate_grocery_list(
        goal=goal,
        dietary_preference=dietary_preference
    )

    return {
        "goal": goal,
        "dietary_preference": dietary_preference,

        "nutrition_targets": nutrition,

        "meal_plan": meals,

        "grocery_list": grocery_list,

        "note": (
            "This is a general nutrition estimate "
            "and not a medical or clinical diet plan."
        )
    }