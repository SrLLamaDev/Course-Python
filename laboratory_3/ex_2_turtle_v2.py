import turtle

t = turtle.Turtle()

# Configurar tamaño del cuadrado
side = 100

t.pensize(3)  # Configurar el grosor del pincel
t.speed(3)
# Dibujar cuadrado con flechas
for _ in range(4):
    t.forward(side - 60)  # Se detiene antes del vértice
    t.penup()
    t.forward(20)  # Espacio vacío en el vértice
    t.pendown()
    t.left(90)

turtle.done()
