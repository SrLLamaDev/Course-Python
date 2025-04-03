def imprimir_tablero(tablero):
    """Imprime el tablero de juego."""
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)


def verificar_ganador(tablero):
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
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]

    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]

    return None


def tablero_completo(tablero):
    """Verifica si el tablero está completo (empate)."""
    for fila in tablero:
        if " " in fila:
            return False
    return True


def jugar_tres_en_raya():
    """Función principal para jugar al "tres en raya"."""
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {turno}.")
        fila = int(input("Ingresa el número de fila (1, 2 o 3): ")) - 1
        columna = int(input("Ingresa el número de columna (1, 2 o 3): ")) - 1

        if tablero[fila][columna] != " ":
            print("Esa casilla ya está ocupada. Intenta nuevamente.")
            continue

        tablero[fila][columna] = turno
        ganador = verificar_ganador(tablero)

        if ganador:
            imprimir_tablero(tablero)
            print(f"¡El jugador {ganador} ha ganado!")
            break
        elif tablero_completo(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X"


# Inicio del juego
print("Bienvenido al juego 'Tres en Raya'!")
jugar_tres_en_raya()
