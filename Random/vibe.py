import random
import time

def vibe_check():
    vibes = [
        "Chill 🌊 – You're radiating calm energy today.",
        "Hype 🔥 – The energy is electric, let's gooo!",
        "Cozy 🧸 – Perfect day for tea and a blanket.",
        "Mystic 🔮 – Something magical is in the air.",
        "Retro 🎵 – Throwback vibes are strong today.",
        "Bold 💥 – Time to take on the world!",
        "Zen 🧘 – Everything is balanced and peaceful.",
        "Chaotic ⚡ – Expect the unexpected!"
    ]
    
    print("Performing vibe check", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

    selected_vibe = random.choice(vibes)
    print("✨ Vibe Detected ✨")
    print(selected_vibe)

if __name__ == "__main__":
    vibe_check()
