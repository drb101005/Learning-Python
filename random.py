import random

# List of words to choose from
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "flamingo", "grape", "honeydew"]

# Function to generate a random word
def generate_random_word():
    return random.choice(words)

# Run the generator
if __name__ == "__main__":
    word = generate_random_word()
    print("Random word:", word)
