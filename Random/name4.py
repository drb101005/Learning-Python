import datetime
import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def loading_effect(text="Loading", dots=3, delay=0.23):
    for i in range(dots):
        print(f"{text}{'.' * (i+1)}", end="\r")
        time.sleep(delay)
    print(" " * 20, end="\r")  # Clear line

def get_time_of_day():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "🌅 Good morning"
    elif 12 <= hour < 17:
        return "🌞 Good afternoon"
    elif 17 <= hour < 21:
        return "🌇 Good evening"
    else:
        return "🌙 Hello night owl"

def get_random_compliment():
    compliments = [
        "You're doing great! 🚀",
        "You have a brilliant mind! 🧠",
        "Keep up the good work! 💪",
        "You're an awesome learner! 📚",
        "You're already better at this than you think! 🌟"
    ]
    return random.choice(compliments)

def get_colored(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

def main():
    print(get_colored("👋 Welcome to the Python Greeter App!\n", Fore.CYAN))

    while True:
        name = input(get_colored("📝 What's your name? ", Fore.YELLOW)).strip()
        if name:
            name = name.title()
            break
        else:
            print(get_colored("⚠️ Please enter a valid name.\n", Fore.RED))

    loading_effect("Thinking")

    greeting = get_time_of_day()
    compliment = get_random_compliment()

    print("\n" + get_colored(f"{greeting}, {name}! 🎉", Fore.GREEN))
    print(get_colored(compliment, Fore.MAGENTA))

# Run the program
if __name__ == "__main__":
    main()
