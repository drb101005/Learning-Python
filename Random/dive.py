import time
import random

# Sea creatures and depths
sea_life = {
    0: "Nothing here",
    50: "🦀 You see a crab scuttling over the sand.",
    30: "🐠 A school of colorful fish swims by.",
    50: "🐙 An octopus blends into a rock.",
    100: "🦑 A squid jets past you in a hurry.",
    200: "🦈 A shark cruises silently nearby.",
    500: "🐋 A massive whale sings in the distance.",
    1000: "🌌 It's nearly pitch black. Bioluminescent jellyfish glow eerily.",
    3000: "🧠 You encounter the mysterious deep-sea gulper eel.",
    6000: "🕳️ You've reached the abyssal zone. Only the toughest survive here.",
}

def dive_simulation():
    depth = 0
    max_depth = 7000
    step = 500

    print("🌊 Starting your deep-sea dive...")
    time.sleep(1)

    while depth <= max_depth:
        print(f"\n📍 Depth: {depth} meters")
        if depth in sea_life:
            print(sea_life[depth])
        elif random.random() < 0.1:
            print("💤 Nothing but silence and darkness...")
        time.sleep(0.8)
        depth += step

    print("\n🚀 Returning to surface...")
    time.sleep(2)
    print("✅ Dive complete. Hope you enjoyed the journey!")

if __name__ == "__main__":
    dive_simulation()
