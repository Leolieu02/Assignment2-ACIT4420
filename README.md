## Overview
Study Reminders is a Python package designed to automate personalized study reminders for students.
The project combines several independent modules managing students, generating reminders, sending notifications, logging activity, and scheduling tasks—into one automated reminder system.

The system can run in two modes:
- Manual mode: Sends reminders immediately (useful for testing).
- Scheduled mode: Automatically sends reminders daily at each student’s preferred time until the user stops the program.

## Installation

Inside the **Assignment 2** folder, install the package locally using the command:
- pip install -e .

## Usage
After installation, run the main program with:
- study-reminders

You will be prompted to choose 1 or 2: 
1. **Immediate run** – Sends all reminders right away. (For testing)
2. **Scheduled run** – Starts the daily scheduler, which keeps running until manually terminated.

## Notes
* Make sure preferred times are formatted in **24-hour `HH:MM`** format (e.g., `10:30`).
* Reminder logs are saved automatically to `reminder_log.txt`.
* Stop the scheduled run manually (e.g., with `Ctrl + C`).
* The program creates a students.json file if it isnt already there

