# Using the init.py file to import all necessary modules for easy access in main.py
from study_reminders import (
    StudentsManager,
    generate_reminder,
    send_reminder,                          
    log_reminder,
    schedule_reminders,
)
from datetime import datetime, timedelta
import time 

def main():
    manager = StudentsManager()
    
    # List students from JSON file 
    print("Current Students:")
    print("")
    manager.list_students()

    # Example: Add a new student
    print("\nAdding a new student...")
    manager.add_student("David", "david@example.com", "Biology", "10:00 AM")
    print("Updated Students List:")
    print("")
    manager.list_students()

    # Example: Remove a student
    manager.remove_student("David")

if __name__ == "__main__":
    main()







