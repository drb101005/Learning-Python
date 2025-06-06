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