import datetime
import random

def get_time_of_day():
    """Returns a greeting based on the time of day."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Hello"

def get_random_compliment():
    """Returns a random compliment."""
    compliments = [
        "You're doing great!",
        "You have a brilliant mind!",
        "Keep up the good work!",
        "You're an awesome learner!",
        "You're already better at this than you think."
    ]
    return random.choice(compliments)

def main():
    print("Welcome to the Python Greeter App!\n")

    # Loop until a valid name is entered
    while True:
        name = input("What's your name? ").strip()
        if name:
            name = name.title()
            break
        else:
            print("Please enter a valid name.")

    # Final greeting
    greeting = get_time_of_day()
    compliment = get_random_compliment()
    print(f"\n{greeting}, {name}!")
    print(compliment)


# Run the program
if __name__ == "__main__":
    main()
