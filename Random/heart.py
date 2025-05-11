import numpy as np
import matplotlib.pyplot as plt

# Parametric heart equation
t = np.linspace(0, np.pi, 1000)  # Only upper half for first quadrant
x_full = 16 * np.sin(t) ** 3
y_full = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Shift and scale to fit in first quadrant
x = (x_full + 17) / 2  # Shift right
y = (y_full + 17) / 2  # Shift up

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')        # Background of figure
ax.set_facecolor('black')               # Background of plot area
ax.plot(x, y, color='red', linewidth=2)

# Grid and axes
ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.set_xlim(0, max(x) + 2)
ax.set_ylim(0, max(y) + 2)
ax.set_aspect('equal')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(colors='white')          # White ticks for contrast
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Optional: label axes
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
