# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder_message = f"Note: '{task}' is a {priority} priority task."

# Use match-case to process the priority level
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level entered. Please choose from 'high', 'medium', or 'low'."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder_message += " That requires immediate attention today!"
elif time_bound == "no":
    reminder_message += " You can complete it when you have time."

# Print the final reminder
print(reminder_message)


