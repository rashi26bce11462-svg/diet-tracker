"""
report.py
------------------
Module 4: Report / Analytics

Generates a simple daily summary combining the BMI result and the
calorie tracker log, gives a basic suggestion, and can save the report
to a text file (also acts as simple logging for the app).
"""

import datetime
import os

REPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")

# Rough daily calorie guideline used only to give a simple suggestion.
# (Not medical advice - just a basic reference point for the project.)
RECOMMENDED_DAILY_CALORIES = 2000


def build_report_text(bmi_result, daily_log, total_calories):
    lines = []
    lines.append("===== DIET TRACKER - DAILY REPORT =====")
    lines.append(f"Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    if bmi_result:
        lines.append(f"BMI: {bmi_result['bmi']} ({bmi_result['category']})")
    else:
        lines.append("BMI: Not calculated this session.")

    lines.append("")
    lines.append("Food Log:")
    if not daily_log:
        lines.append("  No food items logged.")
    else:
        for entry in daily_log:
            lines.append(f"  - {entry['quantity_g']}g {entry['food']}: {entry['calories']} kcal")

    lines.append("")
    lines.append(f"Total Calories Consumed: {total_calories} kcal")
    lines.append(f"Recommended Daily Calories (reference): {RECOMMENDED_DAILY_CALORIES} kcal")

    if total_calories == 0:
        lines.append("Suggestion: No food logged yet today.")
    elif total_calories < RECOMMENDED_DAILY_CALORIES * 0.8:
        lines.append("Suggestion: Your intake looks lower than the reference value.")
    elif total_calories <= RECOMMENDED_DAILY_CALORIES * 1.1:
        lines.append("Suggestion: Your intake is close to the reference value.")
    else:
        lines.append("Suggestion: Your intake is higher than the reference value.")

    lines.append("========================================")
    return "\n".join(lines)


def save_report(report_text):
    """Saves the report text to a timestamped file inside reports/."""
    os.makedirs(REPORT_DIR, exist_ok=True)
    filename = f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(REPORT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(report_text)
    return path


def run_report(bmi_result, daily_log, total_calories):
    """
    Handles user input/output for the Report module (used by main.py menu).
    """
    report_text = build_report_text(bmi_result, daily_log, total_calories)
    print("\n" + report_text)

    save_choice = input("\nSave this report to a file? (y/n): ").strip().lower()
    if save_choice == "y":
        path = save_report(report_text)
        print(f"Report saved to: {path}")
