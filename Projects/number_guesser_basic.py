import random

def guess_the_number():
    print("Welcome to the Random Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            # Ask the user to input their guess
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if player_guess < number_to_guess:
                if (number_to_guess - player_guess) > 10:
                    print("Too Low...")
                else:
                    print("Little Low....")

            elif player_guess > number_to_guess:
                if (player_guess - number_to_guess) > 10:
                    print("Too High...")
                else:
                    print("Little High....")

            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

# Main loop to ask if the player wants to play again
def main():
    while True:
        print("Would you like to play a game?")
        game = int(input("Enter 1 to play and 0 to quit: "))
        
        if game == 1:
            guess_the_number()
        elif game == 0:
            print("Thanks for playing! Goodbye!")
            break  # Exit the loop and end the game
        else:
            print("Invalid input. Please enter 1 to play or 0 to quit.")

# Start the game
main()
