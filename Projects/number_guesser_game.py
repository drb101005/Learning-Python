#This is the  V2 of the number guesser game
# first take input from user for the game level
#first def levelsincluding the impossible one

# parts to add are introduction with the print slow modulet colours
#adding a UI with tink ter)2 options key boord part or add buttons
leved plan 0-5 0-10. 0 to 15 in the last difficulty 0-1 but the random number changes after every wrong attempt

level = int(input ("Enter the level of diffutly you want :))
,
def level1():

    guess = int(input(Style.BRIGHT + Fore.MAGENTA + "Enter your guess (from 0 to ) : "))
    if(guess < number):
        print("Low!")
      
    elif(number < guess):
        print("High!")
        
    else:
        print(Style.BRIGHT + Fore.BLUE + "You guessed the number right!!")
        
        return 0