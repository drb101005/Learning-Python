# A simple game of Rock, Paper, and Scissors
'''
Rock = 1
Paper = 2
Scissors = 3
'''
import random

user_times = int(input("Enter the number of times you want to play : "))
temp = 1



def game():
    user_choice = int(input("Enter your choice (1, 2, 3): "))

    computer = random.choice([1, 2, 3])

    if user_choice == computer:
        print("Draw!!")
    elif(user_choice>3):
        print("Not in option!!")
    else:
        if user_choice == 1 and computer == 2:
            print("You lose!!")  # Rock vs Paper
        elif user_choice == 1 and computer == 3:
            print("You win!!")   # Rock vs Scissors
        elif user_choice == 2 and computer == 1:
            print("You win!!")   # Paper vs Rock
        elif user_choice == 2 and computer == 3:
            print("You lose!!")  # Paper vs Scissors
        elif user_choice == 3 and computer == 1:
            print("You lose!!")  # Scissors vs Rock
        else:
            print("You win!!")   # Scissors vs Paper

while(temp<=user_times):
    game()
    temp = temp + 1
