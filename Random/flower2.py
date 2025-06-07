import turtle
import math
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Beautiful Flower")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Function to draw a single petal
def draw_petal(t, radius, angle):
    t.color("hot pink")
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
    t.end_fill()

# Function to draw the flower
def draw_flower(t, num_petals, radius, angle):
    hue = 0.9  # pinkish hue
    for _ in range(num_petals):
        rgb = colorsys.hsv_to_rgb(hue, 0.6, 1)
        t.color(rgb)
        draw_petal(t, radius, angle)
        t.left(360 / num_petals)

# Draw the flower petals
pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_flower(pen, 12, 100, 60)

# Draw the center
pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.color("gold")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Draw the stem
pen.penup()
pen.goto(0, -40)
pen.setheading(-90)
pen.pendown()
pen.color("green")
pen.width(10)
pen.forward(200)

# Hide turtle
pen.hideturtle()
turtle.done()
