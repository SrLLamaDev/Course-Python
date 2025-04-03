import turtle

# Crear la ventana de juego
ventana = turtle.Screen()
ventana.title("Tres en Raya")
ventana.bgcolor("white")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Crear el tablero de juego
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Crear el lápiz para dibujar en la ventana
lapiz = turtle.Turtle()
lapiz.speed(0)
lapiz.penup()
lapiz.hideturtle()

# Funciones para dibujar el tablero y las marcas
def dibujar_tablero():
    """Dibuja el tablero de juego."""
    lapiz.goto(-150, 150)
    lapiz.pendown()
    for _ in range(4):
        lapiz.forward(300)
        lapiz.right(90)
    lapiz.penup()

def dibujar_marca(fila, columna, marca):
    """Dibuja la marca en la casilla correspondiente."""
    x = columna * 100 - 150
    y = 150 - fila * 100
    lapiz.goto(x, y)
    lapiz.pendown()
    lapiz.write(marca, align="center", font=("Arial", 48, "bold"))
    lapiz.penup()

# Función para manejar los clics del mouse
def manejar_clic(x, y):
    """Maneja los clics del mouse en la ventana."""
    if -150 < x < 150 and -150 < y < 150:
        fila = 2 - int((y + 150) // 100)
        columna = int((x + 150) // 100)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "X" if len(marcas) % 2 == 0 else "O"
            dibujar_marca(fila, columna, tablero[fila][columna])
            ganador = verificar_ganador()
            if ganador:
                turtle.onscreenclick(None)  # Desactivar clics del mouse
                turtle.textinput("Fin del juego", f"¡El jugador {ganador} ha ganado!")
            elif tablero_completo():
                turtle.onscreenclick(None)  # Desactivar clics del mouse
                turtle.textinput("Fin del juego", "¡Empate!")
    else:
        turtle.onscreenclick(None)  # Desactivar clics del mouse

# Función para verificar si hay un ganador
def verificar_ganador():
    """Verifica si hay un ganador en el tablero."""
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] != " ":
            return tablero[0][columna]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    return None

    #verificar si el tabler esta completo
    def tablero_completo():
        """Verifica si el tablero está completo."""
        for fila in tablero:
            if " " in fila:
                return False
        return True
    #Dibujar el tablero inicial
    dibujar_tablero()
    #Activar los clics del mouse
    turtle.mainloop()
