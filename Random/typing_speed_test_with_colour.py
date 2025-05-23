import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def typing_speed_test():
    # Sentence to type
    test_sentence = "The quick brown fox jumps over the lazy dog."
    print(Fore.CYAN + "Typing Speed Test")
    print(Fore.YELLOW + "-.-.-.-.-.-.-.-.-.-")
    print(Fore.GREEN + "Type the following sentence as fast and accurately as you can:\n")
    print(Fore.WHITE + f'"{test_sentence}"\n')
    input(Fore.MAGENTA + "Press Enter when you are ready to start...")

    # Start time
    start_time = time.time()
    typed_sentence = input(Fore.LIGHTBLUE_EX + "\nStart typing: ")
    end_time = time.time()

    # Calculate typing time
    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60

    # Calculate words per minute (WPM)
    word_count = len(test_sentence.split())
    typing_speed = word_count / time_taken_minutes

    # Check for accuracy
    if typed_sentence == test_sentence:
        print(Fore.GREEN + "\nGreat job! You typed it correctly.")
    else:
        print(Fore.RED + "\nOops! There were some mistakes in your typing.")

    # Results
    print(Fore.CYAN + f"\nTime taken: {time_taken:.2f} seconds")
    print(Fore.BLUE + f"Your typing speed is: {typing_speed:.2f} words per minute")

# Run the test
typing_speed_test()
