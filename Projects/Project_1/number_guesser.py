# A simple game to play guess the number

import random
from colorama import Fore, Style, init
i = 0
number = random.choice([1,2,3,4,5,6,7,8,9])

def game():

    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 1 to 9) : "))
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
