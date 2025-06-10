import time
import random

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def launch_bottle():
    print_slow("🌊 Welcome to the Message in a Bottle experience...\n")

    # Get user input
    message = input("📜 What message would you like to send across the sea? \n> ").strip()

    if not message:
        print("\n⚠️  A silent bottle floats empty... Try sending a real message next time.")
        return

    # Create the bottle
    bottle = {
        "material": "old green glass",
        "sealed_with": "wax",
        "message": message,
        "floating": True
    }

    print_slow("\n🧴 You seal the bottle with care...")
    time.sleep(1)
    print_slow("You walk to the edge of the shore...")
    time.sleep(1)
    print_slow("And with a strong throw, you send it into the waves.\n")
    time.sleep(2)

    print_slow("🌊 The bottle begins its journey across the ocean...", delay=0.04)
    for i in range(3):
        print_slow(".", delay=0.8)

    # Random destination
    destinations = [
        "a remote island 🌴",
        "the coast of a distant land 🏖️",
        "a fisherman's boat ⚓",
        "a quiet beach under moonlight 🌕",
        "the hands of a lonely traveler 🚶‍♂️"
    ]
    destination = random.choice(destinations)

    print_slow(f"\n📍 After weeks at sea, your bottle arrives at {destination}.\n")
    print_slow("Someone picks it up and reads your message...")
    time.sleep(1.5)
    print_slow(f"\n💌 The message inside reads:\n\"{bottle['message']}\"\n", delay=0.07)
    print_slow("And just like that, your words live on... 🌊")

# Run the story
launch_bottle()
