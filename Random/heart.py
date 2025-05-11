import numpy as np
import matplotlib.pyplot as plt

# Full heart parametric equations
t = np.linspace(0, 2 * np.pi, 1000)
x_raw = 16 * np.sin(t)**3
y_raw = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Shift and scale to move into first quadrant
x_shifted = x_raw - np.min(x_raw) + 1  # Shift right
y_shifted = y_raw - np.min(y_raw) + 1  # Shift up

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')        # Black figure background
ax.set_facecolor('black')               # Black plot background
ax.plot(x_shifted, y_shifted, color='red', linewidth=2)

# Grid and axis formatting
ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.set_xlim(0, np.max(x_shifted) + 2)
ax.set_ylim(0, np.max(y_shifted) + 2)
ax.set_aspect('equal')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(colors='white')          # White ticks for contrast
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Optional: axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
