import turtle

# Create a turtle pen
pen = turtle.Turtle()

# Set pen color and size
pen.color("blue")
pen.pensize(3)

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move forward by 100 units
    pen.right(90)     # Turn right by 90 degrees

# Hide turtle and display the window
pen.hideturtle()
turtle.done()
