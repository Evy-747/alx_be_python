#daily_reminder.py 

#prompt user for input 
task = input("Describe a task:")
priority = input ("Is the task a (high/medium/low) priority?").lower()
time_bound = input("Is the task time bound (yes/no)?").lower()

#read input and print responses
match priority:
    case "high" | "medium":
        if time_bound == "yes":
            print(f"{task} is an urgent task that requires immediate attention")
        elif time_bound == "no":
            print(f"you can take your time to {task},but do not take too long!")
        else:
            print("yourtime_boudn input is invalid")
        
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority taks that needs deadline observance, check constantly!")
        elif time_bound == "no":
            print(f"you can take all your time but do not forget")
        else:
            print("invalid time_bound input")
            
    case _:
        print("Invalid input for priority")


