import turtle

def draw_triangle(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

def draw_square(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

def draw_rectangle(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rhombus(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(80)
        turtle.left(60)
        turtle.forward(80)
        turtle.left(120)
    turtle.end_fill()

def draw_parallelogram(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(60)
        turtle.left(120)
    turtle.end_fill()

def draw_trapezoid(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(60)
    turtle.right(60)
    turtle.forward(60)
    turtle.right(60)
    turtle.forward(60)
    turtle.end_fill()

def draw_oval(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(0)
    for _ in range(2):
        turtle.circle(50, 90)
        turtle.circle(100, 90)
    turtle.end_fill()

turtle.speed(50)

draw_triangle("blue", -250, 50)
draw_square("red", -100, 150)
draw_rectangle("yellow", 50, 150)
draw_circle("green", 300, 120, 50)
draw_rhombus("yellow", -250, -50)
draw_parallelogram("blue", -100, -50)
draw_trapezoid("green", 80, 0)
draw_oval("red", 320, -100)

turtle.hideturtle()
turtle.done()
