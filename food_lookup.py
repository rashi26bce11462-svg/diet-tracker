"""
food_lookup.py
------------------
Module 2: Food Search & Calorie Lookup

Loads the calorie dataset (CSV) and lets the user search for a food item
by name to see its calories per 100 grams.

Dataset columns expected:
    foodcategory, fooditem, per100grams, cals_per100grams, kj_per100grams

(Same structure as the Kaggle "Calories In Food Items (per 100 Grams)"
dataset by kkhandekar - you can swap data/calories.csv with the full
Kaggle file and this module will still work.)
"""

import csv
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "calories.csv")


def load_food_data(path=DATA_PATH):
    """
    Reads the CSV file and returns a list of dictionaries, one per food item.
    Returns an empty list (with a printed warning) if the file is missing.
    """
    food_list = []
    try:
        with open(path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # normalise calories to a float for easy maths later
                try:
                    row["cals_per100grams"] = float(row["cals_per100grams"])
                except (ValueError, KeyError):
                    row["cals_per100grams"] = 0.0
                food_list.append(row)
    except FileNotFoundError:
        print(f"Error: Could not find dataset file at {path}")
    return food_list


def search_food(food_list, keyword):
    """
    Case-insensitive search for food items whose name contains `keyword`.
    Returns a list of matching rows (dicts).
    """
    keyword = keyword.strip().lower()
    return [item for item in food_list if keyword in item["fooditem"].lower()]


def run_food_lookup(food_list):
    """
    Handles user input/output for the Food Lookup module (used by main.py menu).
    """
    print("\n--- Food Calorie Lookup ---")
    keyword = input("Enter a food name to search (e.g. banana): ")
    matches = search_food(food_list, keyword)

    if not matches:
        print("No matching food item found. Try a different name.")
        return

    print(f"\nFound {len(matches)} match(es):")
    for item in matches:
        print(f"  {item['fooditem']} ({item['foodcategory']}): "
              f"{item['cals_per100grams']} kcal per 100g")


if __name__ == "__main__":
    data = load_food_data()
    print(f"Loaded {len(data)} food items.")
    run_food_lookup(data)
