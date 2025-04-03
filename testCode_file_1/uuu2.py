import random

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para verificar si el tablero está lleno
def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

# Función para realizar el movimiento del jugador
def hacer_movimiento_jugador(tablero):
    while True:
        fila = int(input("Ingresa el número de fila (1-3): ")) - 1
        columna = int(input("Ingresa el número de columna (1-3): ")) - 1
        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
            tablero[fila][columna] = "X"
            break
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

# Función para realizar el movimiento de la computadora
def hacer_movimiento_computadora(tablero):
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            break

# Función principal del juego
def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)

        if jugador_actual == "X":
            hacer_movimiento_jugador(tablero)
        else:
            hacer_movimiento_computadora(tablero)

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print("¡", jugador_actual, "ha ganado!")
            break
        elif tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

# Iniciar el juego
jugar_tres_en_raya()
