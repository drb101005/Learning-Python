import numpy as np
import matplotlib.pyplot as plt

# Settings
num_rolls = 10000

# Simulate dice rolls
die1 = np.random.randint(1, 7, size=num_rolls)
die2 = np.random.randint(1, 7, size=num_rolls)
totals = die1 + die2

# Analyze results
values, counts = np.unique(totals, return_counts=True)

# Display frequencies
for val, count in zip(values, counts):
    print(f"Total {val}: {count} times")

# Plot results (optional)
plt.bar(values, counts, color='skyblue', edgecolor='black')
plt.title("Dice Roll Distribution (2 Dice)")
plt.xlabel("Dice Total")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()
