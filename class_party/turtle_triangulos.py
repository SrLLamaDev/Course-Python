import turtle

def draw_triangle(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.pensize(3)  # Configurar el grosor del pincel
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

turtle.speed(3)

draw_triangle("red", -150, 0)
draw_triangle("green", 0, 0)
draw_triangle("blue", 150, 0)

turtle.done()
