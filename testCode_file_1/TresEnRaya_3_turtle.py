import turtle

# Configuración de la ventana de juego
ventana = turtle.Screen()
ventana.title("Tres en Raya")
ventana.bgcolor("white")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Tablero de juego
tablero = turtle.Turtle()
tablero.speed(0)
tablero.penup()
tablero.hideturtle()
tablero.goto(-150, 200)
tablero.write("TRES EN RAYA", align="center", font=("Arial", 24, "bold"))
tablero.goto(-150, 160)
tablero.write("Turno del Jugador 1", align="center", font=("Arial", 16, "normal"))
tablero.goto(-150, 120)
tablero.write("Jugador 1: X", align="center", font=("Arial", 16, "normal"))
tablero.goto(-150, 80)
tablero.write("Jugador 2: O", align="center", font=("Arial", 16, "normal"))
tablero.goto(-200, -200)
tablero.pendown()
tablero.pensize(4)
for _ in range(4):
    tablero.forward(400)
    tablero.left(90)
tablero.penup()
tablero.hideturtle()

# Lista para almacenar el estado del tablero
estado_tablero = [""] * 9

# Función para dibujar X
def dibujar_x(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(70)
    turtle.backward(140)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.backward(140)
    turtle.forward(70)
    turtle.penup()
    turtle.goto(-150, 160)
    turtle.write("Turno del Jugador 2", align="center", font=("Arial", 16, "normal"))

# Función para dibujar O
def dibujar_o(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(35)
    turtle.penup()
    turtle.goto(-150, 160)
    turtle.write("Turno del Jugador 1", align="center", font=("Arial", 16, "normal"))

# Función para marcar la casilla seleccionada
def marcar_casilla(casilla, jugador):
    x, y = casilla
    index = 0
    if x == -150 and y == 40:
        index = 0
    elif x == -50 and y == 40:
        index = 1
    elif x == 50 and y == 40:
        index = 2
    elif x == -150 and y == -60:
        index = 3
    elif x == -50 and y == -60:
        index = 4
    elif x == 50 and y == -60:
        index = 5
    elif x == -150 and y == -160:
        index = 6
    elif x == -50 and y == -160:
        index = 7
    elif x == 50 and y == -160:
        index = 8

    if estado_tablero[index] == "":
        if jugador == dibujar_x(x, y):
            estado_tablero[index] = "X"
        else:
            dibujar_o(x, y)
            estado_tablero[index] = "O"
#Funcion para verificar si hay ganador
def hay_ganador():
    ganadores = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for ganador in ganadores:
        a, b, c = ganador
        if estado_tablero[a] == estado_tablero[b] == estado_tablero[c] and estado_tablero[a] != "":
            return estado_tablero[a]
    return None
#Funcion para verificar si hay empate
def hay_empate():
    return "" not in estado_tablero
#Funcion para reiniciar el juego
def reiniciar_juego():
    global estado_tablero
    estado_tablero = [""] * 9
    turtle.clear()
    tablero.goto(-150, 160)
    tablero.write("Turno del Jugador 1", align="center", font=("Arial", 16, "normal"))
#Configuracion de eventos
turtle.onscreenclick(lambda x, y: marcar_casilla((x, y), 1), btn=1)
turtle.onscreenclick(lambda x, y: marcar_casilla((x, y), 2), btn=3)
while True:
    ventana.update()
    # Verificar si hay un ganador
    ganador = hay_ganador()
    if ganador:
        tablero.goto(-150, 160)
        tablero.write(f"Ganador: Jugador {ganador}", align="center", font=("Arial", 16, "normal"))
        turtle.onscreenclick(None, btn=1)
        turtle.onscreenclick(None, btn=3)
        turtle.onkey(reiniciar_juego, "r")
        ventana.listen()
        break

    # Verificar si hay empate
    if hay_empate():
        tablero.goto(-150, 160)
        tablero.write("Empate", align="center", font=("Arial", 16, "normal"))
        turtle.onscreenclick(None, btn=1)
        turtle.onscreenclick(None, btn=3)
        turtle.onkey(reiniciar_juego, "r")
        ventana.listen()
        break
