import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# Determine time of day
if 5 <= current_hour < 12:
    time_of_day = "Good morning"
elif 12 <= current_hour < 17:
    time_of_day = "Good afternoon"
elif 17 <= current_hour < 21:
    time_of_day = "Good evening"
else:
    time_of_day = "Hello"

# Ask for the user's name
name = input("What is your name? ").strip().title()

# Check if the user entered something
if name:
    print(f"{time_of_day}, {name}! Welcome to Python.")
else:
    print("Hello! You didn't enter a name, but welcome anyway!")
