import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def animated_dots():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def get_vibe():
    vibes = [
        (Fore.CYAN, "🌊 Chill – You're radiating calm energy."),
        (Fore.RED, "🔥 Hype – The energy is electric, let's gooo!"),
        (Fore.YELLOW, "🧸 Cozy – Perfect day for tea and a blanket."),
        (Fore.MAGENTA, "🔮 Mystic – Something magical is in the air."),
        (Fore.GREEN, "🎵 Retro – Throwback vibes are strong today."),
        (Fore.BLUE, "💥 Bold – Time to take on the world!"),
        (Fore.WHITE, "🧘 Zen – Everything is balanced and peaceful."),
        (Fore.LIGHTRED_EX, "⚡ Chaotic – Expect the unexpected!")
    ]
    return random.choice(vibes)

def vibe_check():
    print(Style.BRIGHT + "🌈 Welcome to the Ultimate Vibe Checker 🌈")
    name = input("What's your name, vibe-seeker? ")

    print(f"\nAlright {name}, sensing your current vibe", end="")
    animated_dots()

    color, message = get_vibe()
    print(color + "✨ Vibe Detected ✨")
    print(color + message + Style.RESET_ALL)

if __name__ == "__main__":
    vibe_check()
