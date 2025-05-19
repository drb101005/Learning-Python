import turtle

# Create a turtle pen
pen = turtle.Turtle()

# Set pen color and size
pen.color("red")
pen.pensize(5)

# Draw a square
for _ in range(800):
    pen.forward(100)  # Move forward by 100 units
    pen.right(90)     # Turn right by 90 degrees
    pen.left(32)
# Hide turtle and display the window
pen.hideturtle()
turtle.done()
