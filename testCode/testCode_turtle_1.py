import turtle

def draw_arrow(t, length, color, angle):
    t.setheading(angle)  # Ajustar la dirección de la flecha
    t.pendown()
    t.color(color)
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
t.pensize(6)  # Flechas más gruesas
t.speed(3)

# Posiciones ajustadas para formar un cuadrado con flechas
positions = [(0, 100), (0, -20), (100, 0), (-20, 0)]  # Flechas verde (arriba), roja (abajo), azul (derecha), amarilla (izquierda)
angles = [0, 0, 90, 90]  # Ángulos de las flechas: arriba, abajo, derecha, izquierda
colors = ["green", "red", "yellow", "blue"]  # Colores de las flechas

# Dibujar cada flecha
for i in range(4):
    t.penup()
    t.goto(positions[i])  # Moverse a la posición
    draw_arrow(t, 80, colors[i], angles[i])  # Dibujar flecha con separación

t.hideturtle()
turtle.done()