import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flower with Turtle")

# Create turtle
flower = turtle.Turtle()
flower.speed(0)
flower.width(2)

# Create a function to draw a flower
def draw_flower(petals, radius):
    h = 0.0  # hue
    for i in range(petals):
        color = colorsys.hsv_to_rgb(h, 1, 1)
        flower.color(color)
        flower.circle(radius)
        flower.left(360 / petals)
        h += 1 / petals

# Position the turtle
flower.penup()
flower.goto(0, -200)
flower.pendown()

# Draw the flower
draw_flower(60, 200)

# Hide the turtle and keep the window open
flower.hideturtle()
turtle.done()
