import turtle

def draw_arrow(t, length, color):
    t.color(color)
    t.pendown()
    t.forward(length - 20)  # Espacio antes de la punta
    t.penup()
    t.forward(20)  # Espacio vacío en el vértice
    t.pendown()
    
    # Dibujar la punta de la flecha
    t.left(150)
    t.forward(15)
    t.backward(15)
    t.right(300)
    t.forward(15)
    t.backward(15)
    t.left(150)

# Configurar tortuga
t = turtle.Turtle()
t.pensize(6)
t.speed(3)

# Posicionar en el centro
t.penup()
t.goto(0, 0)
t.setheading(90)  # Empezar apuntando arriba

# Colores de las flechas
colors = ["blue", "green", "yellow", "red"]

# Dibujar las cuatro flechas
for color in colors:
    draw_arrow(t, 100, color)
    t.right(90)  # Girar para la siguiente flecha

t.hideturtle()
turtle.done()