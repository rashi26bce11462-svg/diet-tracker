# Problem Statement

## Problem Statement
Most people do not track how many calories they consume daily and are
often unaware of their Body Mass Index (BMI) or whether it falls in a
healthy range. Without an easy way to check food calorie content and
track intake, it becomes difficult to make informed dietary decisions.
Diet Tracker addresses this by providing a simple command-line tool to
calculate BMI, look up food calorie content, log daily food intake, and
view a summary report.

## Scope of the Project
- Calculate BMI from user-entered height and weight.
- Look up calorie information for food items from a dataset (per 100g).
- Allow the user to log food eaten during the day with quantity.
- Generate and optionally save a daily summary report.
- Runs as a console/command-line application (no GUI or database).
- Data for the session is stored in memory; reports can be saved as text
  files for a permanent record.

**Out of scope:** user accounts/login, multi-day historical tracking
across sessions, mobile/web interface, personalized medical/nutrition
advice.

## Target Users
- College students and beginners who want a simple, no-frills way to
  monitor their diet and BMI.
- Anyone who wants a lightweight, offline calorie-tracking tool without
  needing an app or internet connection.

## High-Level Features
1. BMI Calculator (height/weight → BMI + category)
2. Food Calorie Lookup (search food dataset)
3. Daily Calorie Tracker (log food + quantity, running total)
4. Daily Report/Summary (combine BMI + food log + suggestion, save to file)
