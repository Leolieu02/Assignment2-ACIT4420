from setuptools import setup, find_packages

setup(
    name="StudyReminders", # The package name
    version="0.2",
    packages=find_packages(), # Automatically find all packages in your project
    include_package_data=True, 
    description="A python package that automates sending study reminders to students based on their courses",
    author="Leo Christopher Lieu",
    author_email="leolieu2002@hotmail.com",
    install_requires=[
        "schedule"
    ],
    
    entry_points={
    'console_scripts': [
        'study-reminders = study_reminders.main:main', # Points to the main function in games/main.py
        ],
    },
)