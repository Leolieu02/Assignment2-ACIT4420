import json

class StudentsManager:
    """Class to manage student data with JSON storage."""

    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        self.students = self.load_students()

    def load_students(self):
        """Load student data from a JSON file."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return [
                {"name": "Alice", "email": "alice@example.com", "course": "Computer Science", "preferred_time": "08:00"},
                {"name": "Bob", "email": "bob@example.com", "course": "Mathematics", "preferred_time": "09:00"},
                {"name": "Charlie", "email": "charlie@example.com", "course": "Physics", "preferred_time": "07:30"}
            ]

    def add_student(self, name, email, course, preferred_time="08:00 AM"):
        """Add a student and save to the JSON file."""
        student = {
            'name': name,
            'email': email,
            'course': course,
            'preferred_time': preferred_time
        }
        self.students.append(student)
        self.save_students()

    def remove_student(self, name):
        """Remove a student by name and update the JSON file."""
        self.students = [s for s in self.students if s['name'] != name]
        self.save_students()

    def save_students(self):
        """Save student data to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(self.students, file, indent=4)

    def get_students(self):
        """Retrieve the list of students."""
        return self.students

    def list_students(self):
        """Print all students."""
        for student in self.students:
            print(f"Name: {student['name']}, Email: {student['email']}, Course: {student['course']}, Preferred Time: {student['preferred_time']}")
