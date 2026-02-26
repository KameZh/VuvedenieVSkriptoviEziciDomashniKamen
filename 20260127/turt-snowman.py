import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Snowman")
screen.bgcolor("sky blue")
pen = turtle.Turtle()
pen.shape("classic")
pen.speed(255)
def goto(x: float, y: float):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
def draw_filled_circle(cx: float, cy: float, r: float, color: str, outline: str = None):
    pen.color(color)
    pen.fillcolor(color)
    pen.pensize(1)
    goto(cx, cy - r)
    pen.setheading(0)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()
    if outline:
        pen.color(outline)
        pen.pensize(4)
        goto(cx, cy - r)
        pen.setheading(0)
        pen.circle(r)
        pen.pensize(1)
def draw_filled_rect(x: float, y: float, w: float, h: float, color: str, outline: str = None):
    pen.fillcolor(color)
    pen.color(color)
    pen.pensize(1)
    goto(x - w/2, y)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()
    if outline:
        pen.color(outline)
        pen.pensize(4)
        goto(x - w/2, y)
        for _ in range(2):
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)
        pen.pensize(1)
def draw_button(x: float, y: float, r: float=5):
    draw_filled_circle(x, y, r, "#111111")
def draw_eye(x: float, y: float, r: float=6):
    draw_filled_circle(x, y, r, "#111111")
def draw_carrot_nose(x: float, y: float, length: float=30, height: float=10):
    pen.color("orange")
    pen.fillcolor("orange")
    goto(x, y + height/2)
    pen.begin_fill()
    pen.setheading(0)
    pen.goto(x + length, y)
    pen.goto(x, y - height/2)
    pen.goto(x, y + height/2)
    pen.end_fill()
def draw_arm(x1: float, y1: float, x2: float, y2: float, branches: list):
    pen.color("sienna")
    pen.pensize(5)
    goto(x1, y1)
    pen.setheading(pen.towards(x2, y2))
    pen.goto(x2, y2)
    for bx, by in branches:
        goto(x2, y2)
        pen.goto(bx, by)
    pen.pensize(1)
def draw_snowflake(x: float, y: float, size: float):
    pen.color("white")
    pen.pensize(2)
    goto(x, y)
    for _ in range(6):
        pen.forward(size)
        pen.backward(size)
        pen.right(60)
    pen.pensize(1)
def draw_tree(x: float, y: float, trunk_h: float, tree_h: float):
    pen.color("#3d2817")
    pen.fillcolor("#3d2817")
    goto(x - 8, y)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(16)
        pen.left(90)
        pen.forward(trunk_h)
        pen.left(90)
    pen.end_fill()
    pen.color("#1a472a")
    pen.fillcolor("#1a472a")
    goto(x - tree_h * 0.6, y + trunk_h)
    pen.begin_fill()
    pen.goto(x, y + trunk_h + tree_h)
    pen.goto(x + tree_h * 0.6, y + trunk_h)
    goto(x - tree_h * 0.6, y + trunk_h)
    pen.end_fill()
for _ in range(25):
    sx = random.randint(-350, 350)
    sy = random.randint(-100, 280)
    ssize = random.randint(5, 12)
    draw_snowflake(sx, sy, ssize)
tree_positions = [
    (-320, -240, 30, 80),
    (-270, -240, 25, 70),
    (-220, -240, 35, 90),
    (-170, -240, 28, 75),
    (170, -240, 30, 85),
    (220, -240, 25, 65),
    (270, -240, 32, 80),
    (320, -240, 28, 70),
]
for tx, ty, th, tt in tree_positions:
    draw_tree(tx, ty, th, tt)

draw_filled_circle(0, -160, 80, "white", "black")
draw_filled_circle(0, -60, 60, "white", "black")
draw_filled_circle(0, 20, 40, "white", "black")

for by in (-35, -55, -75, -95):
    draw_button(0, by, 6)

for by in (-135, -165):
    draw_button(0, by, 6)

draw_eye(-15, 35, 6)
draw_eye(15, 35, 6)

draw_carrot_nose(0, 20, length=35, height=12)

pen.color("black")
pen.pensize(3)
goto(-12, 5)
pen.setheading(-60)
pen.circle(15, 120)
pen.pensize(1)

draw_arm(-40, -25, -120, 10, branches=[(-110, 25), (-135, -5)])
draw_arm(40, -25, 120, 10, branches=[(110, 25), (135, -5)])
draw_filled_rect(0, 38, 100, 8, "#222222", "black")
draw_filled_rect(0, 46, 60, 45, "#333333", "black")

turtle.done()