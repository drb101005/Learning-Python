import numpy as np
import matplotlib.pyplot as plt

# Define x range where the expression under the square root is non-negative
x = np.linspace(-1, 3, 400)
under_sqrt = 2 * x - x**2

# Valid domain where y^2 = 2x - x^2 is non-negative
valid = under_sqrt >= 0
x_valid = x[valid]
y_valid = np.sqrt(under_sqrt[valid])

# Plot both positive and negative roots
plt.figure(figsize=(6, 6))
plt.plot(x_valid, y_valid, label='Positive root')
plt.plot(x_valid, -y_valid, label='Negative root')



plt.title(r'Graph of $y^2 + x^2 = 2x$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='gray', linewidth=0.500)
plt.axvline(0, color='gray', linewidth=0.500)
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
