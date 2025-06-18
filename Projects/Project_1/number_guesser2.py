# A simple game to play guess the number

import random
import time
from colorama import Fore, Style, init

init(autoreset=True)
i = 0

# Animated welcome message
welcome_msg = "Welcome to Guess the Number!"
for char in welcome_msg:
    print(Fore.CYAN + Style.BRIGHT + char, end='', flush=True)
    time.sleep(0.05)
print("\n")

print(Fore.YELLOW + Style.BRIGHT + "Levels:\n1. Easy (0-5)\n2. Medium (0-9)\n3. Hard (0-15)\n4. Impossible (0-9 with changing number)\n")

difficulty_level = int(input(Fore.GREEN + "Enter the level of difficulty from 1, 2, 3, or 4: "))

number1 = random.choice([0, 1, 2, 3, 4, 5])
number2 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
number3 = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

def game1():
    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 5): "))
    if guess < number1:
        print("Low!")
    elif number1 < guess:
        print("High!")
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        return 0

def game2():
    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 9): "))
    if guess < number2:
        print("Low!")
    elif number2 < guess:
        print("High!")
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        return 0

def game3():
    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 15): "))
    if guess < number3:
        print("Low!")
    elif number3 < guess:
        print("High!")
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        return 0

def impossible():
    number = random.randint(0, 9)
    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 9): "))
    if guess < number:
        print("Low!")
    elif number < guess:
        print("High!")
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        return 0

if difficulty_level == 1:
    while True:
        i += 1
        if game1() == 0:
            print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
            break

elif difficulty_level == 2:
    while True:
        i += 1
        if game2() == 0:
            print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
            break

elif difficulty_level == 3:
    while True:
        i += 1
        if game3() == 0:
            print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
            break

elif difficulty_level == 4:
    while True:
        i += 1
        if impossible() == 0:
            print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
            break
