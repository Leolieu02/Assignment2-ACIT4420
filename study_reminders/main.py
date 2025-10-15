from .students_manager import StudentsManager
from .reminder_generator import generate_reminder
from .reminder_sender import send_reminder
from .scheduler import schedule_reminders
from .logger import log_reminder

from datetime import datetime, timedelta
import time 

def main():
    manager = StudentsManager()

    # List students from JSON file 
    print("Current Students:")
    print("")
    manager.list_students()
    print("--------------------------------------------")


    # Example: Add a new students
    print("\nAdding a new students...")
    manager.add_student("David", "david@example.com", "Biology", "13:17") # Should have a time that format HH:MM and not have AM or PM
    manager.add_student("Esther", "esther@example.com", "Privacy", "10:30") # Will be deleted later


    # Example: Updated student list 
    print("Updated Students List:")
    print("")
    manager.list_students()
    print("--------------------------------------------")


    # Example: Remove latest student 
    manager.remove_student("Esther")


    # Example: Updated student list 
    print("Updated list after deleted student:")
    print("")
    manager.list_students()
    print("--------------------------------------------")


    # Schedule reminders for all students
    print("\nScheduling reminders...")
    print("Options")
    print("1. Send reminders now")
    print("2. Start daily scheduler")
    choice = input("Choose an option (1 or 2): ")

    # Run manual (aka for testing)
    if choice == "1":
        print("Sending reminders now...")
        # Loop through all students and send reminders manually 
        for student in manager.get_students():
            reminder = generate_reminder(student['name'], student['course'])
            send_reminder(student['email'], reminder)
            log_reminder(student, reminder)
        print("\nReminders sent and logged successfully.")

    # Run scheduler (for actual use)
    elif choice == "2":
        print("Starting daily scheduler...")
        try:
            # Try to actually run the scheduler
            schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)
        except KeyboardInterrupt:
            # Stop the scheduler when Ctrl+C is pressed
            print("\nScheduler stopped.")
    # Print error message for invalid input
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()







