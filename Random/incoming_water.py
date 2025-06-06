import time
import random

# Constants
SAFE_LEVEL = 5      # Safe water level
DANGER_LEVEL = 10   # Danger threshold

# Initial water level
water_level = 0

print("Monitoring Incoming Water...\n")

while water_level < DANGER_LEVEL:
    increase = random.uniform(0.5, 1.5)  # Simulate rising water
    water_level += round(increase, 2)
        print(f"Current water level: {water_level} meters")

    if water_level >= SAFE_LEVEL and water_level < DANGER_LEVEL:
        print("⚠️ Warning: Water level is getting high!")
           time.sleep(1)  # Pause for effect

print("\n🚨 Danger! Water level has reached a critical point!")
    