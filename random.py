import time

# List of words to choose from
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "flamingo", "grape", "honeydew"]

# Function to generate a pseudo-random word using current time
def generate_random_word():
    current_time = time.time()
    # Get fractional part of current time and multiply it to get more variability
    fractional = current_time - int(current_time)
    mixed_value = int(fractional * 1000000)  # Get microseconds
    index = mixed_value % len(words)
    return words[index]

# Run the generator
if __name__ == "__main__":
    word = generate_random_word()
    print("Random word:", word)
