import numpy as np

# Create two arrays (vectors) with the same shape
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
addition = np.add(array1, array2)
print("Element-wise Addition:", addition)

# Element-wise subtraction
subtraction = np.subtract(array1, array2)
print("Element-wise Subtraction:", subtraction)

# Element-wise multiplication
multiplication = np.multiply(array1, array2)
print("Element-wise Multiplication:", multiplication)

# Element-wise division
division = np.divide(array1, array2)
print("Element-wise Division:", division)

# Dot product of the two arrays
dot_product = np.dot(array1, array2)
print("Dot Product:", dot_product)

# Cross product of the two arrays
cross_product = np.cross(array1, array2)
print("Cross Product:", cross_product)