 # reminder_sender.py
def send_reminder(email, reminder):
    """Simulate sending a reminder to the specified email."""
    if not email:
        raise ValueError("Email address is missing")
    print(f"Sending reminder to {email}: {reminder}")