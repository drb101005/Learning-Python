# # A simple game to play guess the number

# import random
# from colorama import Fore, Style, init
# i = 0
# number1 = random.choice[(0,1,2,3,4,5)]
# number2 = random.choice([0,1,2,3,4,5,6,7,8,9])
# number3 = random.choice[(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)]
#  = int(input("Enter the level of difficulty from level 1,2,3 :"))
# # The plan is to ask user What difficulty he  wants ,in number make 3 types first 0-5 then O to 9, then 0 to 15 
# # add an impossible difficulty where the numbers are from 0 to 9 but after every wrong guess the choice of number changes

# ####Due to the current code syntax , each part has its own while command to run it ,but that has been. changed but I have a feeling theat there is some  mistake in it

# def game1():

#     guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 5) : "))
#     if(guess < number1):
#         print("Low!")
      
#     elif(number1 < guess):
#         print("High!")
        
#     else:
#         print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
#         return 0

# while diffucult_level = 1:
#     i = i + 1
#     if game1() == 0:
       
#         print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
#         break



# def game2():

#     guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 9) : "))
#     if(guess < number2):
#         print("Low!")
      
#     elif(number2 < guess):
#         print("High!")
        
#     else:
#         print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
#         return 0

# while diffucult_level = 2:
#     i = i + 1
#     if game() == 0:
       
#         print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
#         break

# def game3():

#     guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 15) : "))
#     if(guess < number3):
#         print("Low!")
      
#     elif(number3 < guess):
#         print("High!")
        
#     else:
#         print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
#         return 0

# while diffucult_level = 3:
#     i = i + 1
#     if game() == 0:
       
#         print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
#         break


# def impossible():

#     guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to 9) : "))
#     if(guess < number):
#         print("Low!")
# #gotta put the random number choosing thingies here
      
#     elif(number < guess):
#         print("High!")
        
#     else:
#         print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
#         return 0

# while diffucult_level = 1:
#     i = i + 1
#     if impossible() == 0:
       
#         print(Style.BRIGHT + Fore.RED + f"It took you {i} times...")
#         break



# # ask the user if there are multiplayers
# #add difficulties
# # add a little rules and welcome msg ,in that add animations to the welcome msg with colours and fading and all...
