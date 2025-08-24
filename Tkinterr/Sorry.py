import tkinter as tk
import random
import time
import math

# --- Flower Drawing Function ---
def draw_flower(canvas, x, y, size=20):
    colors = ["#FFB6C1", "#FF69B4", "#FFDAB9", "#FFFACD", "#E6E6FA", "#87CEFA"]  # pastel colors
    petal_color = random.choice(colors)
    # Draw petals
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        dx = x + size * 1.5 * math.cos(rad)
        dy = y + size * 1.5 * math.sin(rad)
        canvas.create_oval(dx - size, dy - size, dx + size, dy + size, fill=petal_color, outline="")
    # Draw center
    canvas.create_oval(x - size/2, y - size/2, x + size/2, y + size/2, fill="gold", outline="")

# --- Animation Loop ---
def animate():
    # Draw all flowers first (background)
    for i in range(25):  
        while True:
            x = random.randint(50, 550)
            y = random.randint(50, 350)
            # ✅ Keep flowers away from text area
            if not (200 < x < 400 and 150 < y < 250):
                break
        draw_flower(canvas, x, y, size=random.randint(12, 22))
        window.update()
        time.sleep(0.15)
    
    # ✅ Draw text LAST so it's always on top
    text_id = canvas.create_text(300, 200, text="Enter the name here 💖", font=("Comic Sans MS", 32, "bold"), fill="")
    fade_in_text(canvas, text_id, ["#ffb6c1", "#ff8da1", "#ff5c8a", "#ff1493"])

# --- Fade-in effect ---
def fade_in_text(canvas, text_id, colors):
    for color in colors:
        canvas.itemconfig(text_id, fill=color)
        window.update()
        time.sleep(0.5)

# --- Main Tkinter Window ---
window = tk.Tk()
window.title("Cute Apology")
window.geometry("600x400")
window.config(bg="white")

canvas = tk.Canvas(window, width=600, height=400, bg="white", highlightthickness=0)
canvas.pack()

window.after(500, animate)
window.mainloop()
