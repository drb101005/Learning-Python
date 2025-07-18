#An aim trainer game

import tkinter as tk
import random

class CatchTheDot:
    def __init__(self, master):
        self.master = master
        master.title("Aim Trainer")

        # Game stats
        self.score = 0
        self.misses = 0
        self.max_misses = 10
        self.dot_radius = 15
        self.speed_ms = 7500
        #Change the above line to alter the speed        

        # Widgets
        self.label = tk.Label(master, text="Score: 0", font=("Segoe UI", 14))
        self.label.pack()

        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack()

        # Create the dot (oval)
        self.dot = None
        self.spawn_dot()

        # Bind click event
        self.canvas.bind("<Button-1>", self.on_click)

    def spawn_dot(self):
        # Place the dot at a new random position
        if self.dot:
            self.canvas.delete(self.dot)

        x = random.randint(self.dot_radius, 400 - self.dot_radius)
        y = random.randint(self.dot_radius, 300 - self.dot_radius)
        self.dot = self.canvas.create_oval(
            x - self.dot_radius, y - self.dot_radius,
            x + self.dot_radius, y + self.dot_radius,
            fill="red", outline="black"
        )

        # Schedule next move
        self.master.after(self.speed_ms, self.spawn_dot)

    def on_click(self, event):
        # Handle mouse click on the canvas
        items = self.canvas.find_withtag("current")
        if items and items[0] == self.dot:
            self.score += 10
            self.label.config(text=f"Score: {self.score}")
            # Immediately move the dot
            self.spawn_dot()
        else:
            self.misses += 1
            if self.misses >= self.max_misses:
                self.end_game()

    def end_game(self):
        """Display final score and close after 3 seconds."""
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(
            200, 150, text=f"Game Over!\nFinal Score: {self.score}",
            font=("Segoe UI", 20), fill="black"
        )
        self.master.after(6000, self.master.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheDot(root)
    root.mainloop()
