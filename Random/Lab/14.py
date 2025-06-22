import numpy as np

# 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print("one Dimensional array:")
print(arr1)

# 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Two Dimensional array:")
print(arr2)

# 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print("Three Dimensional array:")
print(arr3)

# Reshaping
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr = arr.reshape(3, 3)
print("Reshaping an array\n", newarr)

# Slicing
array1 = np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
print("slice from index 2 to index 6:", array1[2:6])
print("slice from index 0 to index 8 (exclusive) with a step size of 2:", array1[0:8:2])
print("slice array1 from index 3 up to the last element", array1[3:])
print("slice the last 3 elements of the array", array1[-3:])
print("slice elements from 2nd-to-last to 4th-to-last element", array1[-5:-2])

# Array Indexing
array1 = np.array([1, 3, 5, 7, 9])
print("position 0", array1[0])
print("position 2", array1[2])
print("position 4", array1[4])

array1[2] = 12
print("After modifying first element:", array1)

# Negative Indexing
print("Negative Indexing:", array1[-2])

# 2D array
array2 = np.array([[1, 3, 5], [7, 9, 2], [4, 6, 8]])

# Indexing in 2D Array
print("Indexing in 2D Array:", array2[1, 0])  # prints 7
print("Indexing in 2D Array:", array2[2, 1])  # prints 6