import time

def typing_speed_test():
    # Sentence to type
    test_sentence = ""
    print("Typing Speed Test")
    print("------------------")
    print("Type the following sentence as fast and accurately as you can:\n")
    print(f'"{test_sentence}"\n')
    input("Press Enter when you are ready to start...")

    # Start time
    start_time = time.time()
    typed_sentence = input("\nStart typing: ")
    end_time = time.time()

    # Calculate typing time
    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60

    # Calculate words per minute (WPM)
    word_count = len(test_sentence.split())
    typing_speed = word_count / time_taken_minutes

    # Check for accuracy
    if typed_sentence == test_sentence:
        print("\nGreat job! You typed it correctly.")
    else:
        print("\nOops! There were some mistakes in your typing.")

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Your typing speed is: {typing_speed:.2f} words per minute")

# Run the test
typing_speed_test()
