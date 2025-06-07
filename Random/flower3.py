import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Beautiful Flower Scene")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Draw a single petal
def draw_petal(t, radius, angle, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
    t.end_fill()

# Draw full flower
def draw_flower(t, num_petals, radius, angle):
    hue = 0.9  # Start from a pinkish color
    for _ in range(num_petals):
        rgb = colorsys.hsv_to_rgb(hue, 0.7, 1)
        hex_color = '#%02x%02x%02x' % tuple(int(i * 255) for i in rgb)
        draw_petal(t, radius, angle, hex_color)
        t.left(360 / num_petals)
        hue += 0.02

# Draw center of the flower
def draw_center(t, radius, color):
    t.penup()
    t.goto(0, -radius // 2)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw stem
def draw_stem(t, length):
    t.penup()
    t.goto(0, -20)
    t.setheading(-90)
    t.pendown()
    t.color("green")
    t.width(12)
    t.forward(length)

# Draw leaf
def draw_leaf(t, position, side='left'):
    t.penup()
    t.goto(position)
    t.setheading(-45 if side == 'left' else -135)
    t.pendown()
    t.fillcolor("forest green")
    t.begin_fill()
    t.circle(40, 90)
    t.left(90)
    t.circle(40, 90)
    t.end_fill()

# Draw flower
pen.penup()
pen.goto(0, 0)
pen.setheading(0)
pen.pendown()
draw_flower(pen, num_petals=24, radius=100, angle=60)
draw_center(pen, radius=25, color="gold")
draw_stem(pen, length=300)
draw_leaf(pen, position=(0, -100), side='left')
draw_leaf(pen, position=(0, -180), side='right')

# Finish
turtle.done()

