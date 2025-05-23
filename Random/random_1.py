import time

# List of words to choose from
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "flamingo", "grape", "honeydew"]

def generate_random_word():
    # Get the current time in microseconds
    current_time = str(time.time()).replace('.', '')
    
    # Convert part of that string to an integer
    numeric_seed = int(current_time[-6:])  # Last 6 digits
    
    # Use modulo to get index within range
    index = numeric_seed % len(words)
    
    return words[index]

# Run the function
if __name__ == "__main__":
    word = generate_random_word()
    print("Random word:", word)
