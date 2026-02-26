import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("white")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def circle_filled(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def rectangle(w, h, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

# ================= BODY =================
go(0, -180)
circle_filled(140, "white")

# ================= BUTTONS =================
t.color("black")
for y in (-80, -120):
    go(0, y)
    circle_filled(8, "#3a2f3d")

# ================= HEAD =================
go(0, 20)
circle_filled(100, "white")

# ================= EYES =================
for x in (-30, 30):
    go(x, 60)
    circle_filled(8, "black")

# ================= NOSE =================
go(0, 40)
t.color("black")
t.fillcolor("orange")
t.begin_fill()
t.setheading(0)
t.forward(40)
t.left(120)
t.forward(20)
t.left(120)
t.forward(20)
t.end_fill()

# ================= SCARF =================
go(-100, 10)
rectangle(200, 30, "#f04b3a")

# scarf tail
go(60, -20)
rectangle(30, 70, "#f04b3a")

# ================= ARMS =================
t.pensize(5)
t.color("black")

# left arm
go(-90, -30)
t.setheading(200)
t.forward(90)

# right arm
go(90, -30)
t.setheading(-20)
t.forward(90)

t.pensize(1)

# ================= MITTENS =================
for (x, y) in [(-160, -80), (160, -80)]:
    go(x, y)
    circle_filled(25, "#f04b3a")

# ================= HAT =================
go(-70, 120)
rectangle(140, 20, "#4b3b4f")

go(-50, 140)
rectangle(100, 70, "#4b3b4f")

# ================= DONE =================
turtle.done()
