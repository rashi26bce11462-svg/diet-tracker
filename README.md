# Diet Tracker (Calorie Counter + BMI Calculator)

## Overview
Diet Tracker is a Python command-line application that helps users
monitor their daily calorie intake and check their Body Mass Index (BMI).
It uses a food calorie dataset (based on the Kaggle "Calories In Food
Items (per 100 Grams)" dataset) to look up calories for food items and
lets the user log what they eat throughout the day.

This project was built as part of the VITyarthi "Build Your Own Project"
evaluation.

## Features
- **BMI Calculator** — enter height and weight to get your BMI and category
  (Underweight / Normal / Overweight / Obese).
- **Food Calorie Lookup** — search any food item and see its calories per
  100 grams from the dataset.
- **Daily Calorie Tracker** — log food items with quantity (in grams) and
  get a running total of calories consumed.
- **Daily Report** — view a summary combining BMI, all logged food items,
  and total calories, with a basic suggestion. Reports can be saved to a
  text file for record-keeping.
- **Error Handling** — invalid inputs (negative numbers, letters instead
  of numbers, unknown food items) are handled gracefully without crashing.

## Technologies / Tools Used
- Python 3 (standard library only — `csv`, `os`, `datetime`)
- No external dependencies required
- Git & GitHub for version control

## Project Structure
```
diet-tracker/
├── README.md
├── statement.md
├── data/
│   └── calories.csv          # food calorie dataset
├── src/
│   ├── main.py                # entry point / menu
│   ├── bmi_calculator.py      # Module 1: BMI calculator
│   ├── food_lookup.py         # Module 2: food search
│   ├── calorie_tracker.py     # Module 3: daily calorie logging
│   └── report.py              # Module 4: report/summary generation
├── tests/
│   └── test_bmi.py            # basic tests
├── diagrams/                  # architecture, workflow, use-case diagrams
└── reports/                   # saved daily reports (created at runtime)
```

## Steps to Install & Run
1. Make sure Python 3.8+ is installed on your system.
2. Clone this repository:
   ```
   git clone <your-repo-url>
   cd diet-tracker
   ```
3. (Optional) Replace `data/calories.csv` with the full Kaggle dataset
   ["Calories In Food Items (per 100 Grams)"](https://www.kaggle.com/datasets/kkhandekar/calories-in-food-items-per-100-grams)
   for more food items — keep the same column names.
4. Run the program:
   ```
   cd src
   python main.py
   ```
5. Use the on-screen menu (1–5) to calculate BMI, search food, log meals,
   and view your daily report.

## Instructions for Testing
Run the basic test file to verify the BMI module works correctly:
```
python tests/test_bmi.py
```
All tests print `passed` on success and check things like:
- correct BMI calculation
- correct BMI category classification
- invalid input (zero/negative values) raising an error

## Screenshots
(Add terminal screenshots here after running the program, e.g. the menu,
a BMI result, and a sample daily report.)

## Notes
- The bundled `data/calories.csv` is a smaller sample dataset (~50 items)
  so the project works immediately without downloading anything. Swapping
  in the full Kaggle dataset does not require any code changes.
- The 2000 kcal "recommended daily calories" figure used in the report is
  a general reference value for demonstration, not personalized medical
  advice.
