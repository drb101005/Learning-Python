import time

# List of words to choose from
words = ["apple", "banana", "cherry", "dragonfruit", "elephant", "flamingo", "grape", "honeydew"]

# Function to generate a pseudo-random index using current time
def generate_random_word():
    current_time = time.time()
    index = int(current_time) % len(words)
    return words[index]


if __name__ == "__main__":
 word = generate_random_word()
  print("Random word:", word)
