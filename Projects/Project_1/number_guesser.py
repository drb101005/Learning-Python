# A simple game to play guess the number

import random
from colorama import Fore, Style, init
i = 0
number1 = random.choice[(0,1,2,3,4,5)]
number2 = random.choice([0,1,2,3,4,5,6,7,8,9])
number3 = rancomd.choice[(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)]
# The plan is to ask user What difficulty he  wants ,in number make 3 types first 0-5 then O to 9, then 0 to 15 
# add an impossible difficulty where the numbers are from 0 to 9 but after every wrong guess the choice of number changes

def game1():

    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 5) : "))
    if(guess < number):
        print("Low!")
      
    elif(number < guess):
        print("High!")
        
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
        return 0

while True:
    i = i + 1
    if game() == 0:
       
        print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
        break



def game2():

    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 9) : "))
    if(guess < number):
        print("Low!")
      
    elif(number < guess):
        print("High!")
        
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
        return 0

while True:
    i = i + 1
    if game() == 0:
       
        print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
        break

# ask the user if there are multiplayers
#add difficulties
