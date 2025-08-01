import numpy as np

# 1. Creating arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
eye = np.eye(3)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

# 2. Array indexing and slicing
print("First row of b:", b[0])
print("Element at (1,2):", b[1, 2])
print("Last column:", b[:, -1])

# 3. Array math
c = np.array([10, 20, 30])
print("a + c:", a + c)
print("a * 2:", a * 2)
print("Element-wise multiplication:", a * c)
print("Dot product:", np.dot(a, c))

# 4. Broadcasting
scalar = 5
print("a + scalar:", a + scalar)
matrix = np.array([[1], [2], [3]])
print("Broadcasted addition:\n", matrix + a)

# 5. Aggregations
print("Sum of a:", np.sum(a))
print("Mean of b:", np.mean(b))
print("Max of b:", np.max(b))
print("Argmax of b:", np.argmax(b))

# 6. Reshaping
reshaped = b.reshape(3, 2)
flattened = b.flatten()
transposed = b.T

# 7. Stacking
stacked_v = np.vstack([a, c])
stacked_h = np.hstack([a, c])

# 8. Boolean masking
mask = a > 1
print("Mask:", mask)
print("Filtered values:", a[mask])

# 9. Random numbers
rand_array = np.random.rand(2, 2)
rand_ints = np.random.randint(0, 10, size=(3, 3))
np.random.seed(42)  # Reproducibility

# 10. Linear Algebra
mat = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(mat)
det = np.linalg.det(mat)
eigvals, eigvecs = np.linalg.eig(mat)

# Print all for demonstration
print("Original array a:", a)
print("2D array b:\n", b)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Eye:\n", eye)
print("Arange:", arange)
print("Linspace:", linspace)
print("Reshaped:\n", reshaped)
print("Flattened:", flattened)
print("Transposed:\n", transposed)
print("Stacked vertically:\n", stacked_v)
print("Stacked horizontally:", stacked_h)
print("Random array:\n", rand_array)
print("Random integers:\n", rand_ints)
print("Matrix inverse:\n", inv)
print("Determinant:", det)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
