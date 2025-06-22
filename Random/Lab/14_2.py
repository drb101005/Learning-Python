import numpy as np

array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Function to calculate statistics for a single array
# Mean
mean = np.mean(array)
print(f"Mean: {mean}")

# Median
median = np.median(array)
print(f"Median: {median}")

# Standard Deviation
std_dev = np.std(array)
print(f"Standard Deviation: {std_dev}")

# Variance
variance = np.var(array)
print(f"Variance: {variance}")