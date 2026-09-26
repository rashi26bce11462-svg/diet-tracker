"""
bmi_calculator.py
------------------
Module 1: BMI (Body Mass Index) Calculator

Functions:
    calculate_bmi(weight_kg, height_cm) -> float
    get_bmi_category(bmi) -> str
    run_bmi_calculator() -> dict
"""


def calculate_bmi(weight_kg, height_cm):
    """
    Calculates BMI using the standard formula:
        BMI = weight(kg) / (height(m))^2

    Raises ValueError if inputs are not positive numbers.
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """
    Returns the WHO-style BMI category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def run_bmi_calculator():
    """
    Handles user input/output for the BMI module (used by main.py menu).
    Returns a dict with bmi and category so other modules (like report.py)
    can reuse the result. Returns None if the user enters invalid input.
    """
    print("\n--- BMI Calculator ---")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

        return {"weight": weight, "height": height, "bmi": bmi, "category": category}

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric, positive values.")
        return None


# Quick manual test when this file is run directly
if __name__ == "__main__":
    result = run_bmi_calculator()
    print(result)
