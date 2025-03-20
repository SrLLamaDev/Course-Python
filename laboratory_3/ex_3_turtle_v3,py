import turtle
import math

# Solicitar datos al usuarioaa
'''
view more about documentation of python, for use protocol python are deprecated, find the solution in other version of python: this is note
'''
x, y = map(float, input("Ingrese el centro (x y): ").split())
radio = float(input("Ingrese el radio: "))

# Calcular el área
area = math.pi * (radio ** 2)
print(f"El área del círculo es: {area:.2f}")

# Configurar turtle
t = turtle.Turtle()
t.pensize(3)  # Configurar el grosor del pincel
t.speed(3)
t.pencolor("blue")
t.penup()
t.goto(x, y - radio)  # Mover al punto donde comienza el círculo
t.pendown()

# Dibujar el círculo
t.circle(radio)

# Mostrar el resultado
turtle.done()
