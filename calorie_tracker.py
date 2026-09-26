"""
calorie_tracker.py
------------------
Module 3: Daily Calorie Tracker

Lets the user log food items they ate (with quantity in grams) during the
day. Looks up each item's calories in the dataset and keeps a running
total for the session.
"""

from food_lookup import search_food


def add_food_entry(food_list, daily_log):
    """
    Asks the user for a food name and quantity (in grams), finds it in the
    dataset, calculates the calories for that quantity, and appends an
    entry to daily_log (a list of dicts).
    """
    keyword = input("Enter food item you ate: ")
    matches = search_food(food_list, keyword)

    if not matches:
        print("Food item not found in dataset. Entry not added.")
        return

    # If multiple matches, let the user pick one
    if len(matches) > 1:
        print("Multiple matches found:")
        for i, item in enumerate(matches, start=1):
            print(f"  {i}. {item['fooditem']} ({item['foodcategory']})")
        try:
            choice = int(input("Select the number of the correct item: "))
            selected = matches[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Entry not added.")
            return
    else:
        selected = matches[0]

    try:
        quantity = float(input(f"Enter quantity eaten (in grams) of {selected['fooditem']}: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity. Entry not added.")
        return

    calories_for_quantity = round((selected["cals_per100grams"] / 100) * quantity, 2)

    entry = {
        "food": selected["fooditem"],
        "quantity_g": quantity,
        "calories": calories_for_quantity,
    }
    daily_log.append(entry)
    print(f"Added: {quantity}g of {selected['fooditem']} = {calories_for_quantity} kcal")


def get_total_calories(daily_log):
    """Returns the sum of calories of all entries logged so far."""
    return round(sum(entry["calories"] for entry in daily_log), 2)


def run_calorie_tracker(food_list, daily_log):
    """
    Handles user input/output for the Calorie Tracker module (used by main.py menu).
    """
    print("\n--- Daily Calorie Tracker ---")
    add_food_entry(food_list, daily_log)
    print(f"Running total for today: {get_total_calories(daily_log)} kcal")
