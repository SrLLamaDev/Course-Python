import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana de juego
ANCHO_VENTANA = 300
ALTO_VENTANA = 300
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Tres en Raya')

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración del tablero de juego
TABLERO = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

# Jugador actual
jugador_actual = 'X'

# Función para dibujar el tablero
def dibujar_tablero():
    VENTANA.fill(BLANCO)
    pygame.draw.line(VENTANA, NEGRO, (100, 0), (100, 300), 3)
    pygame.draw.line(VENTANA, NEGRO, (200, 0), (200, 300), 3)
    pygame.draw.line(VENTANA, NEGRO, (0, 100), (300, 100), 3)
    pygame.draw.line(VENTANA, NEGRO, (0, 200), (300, 200), 3)

    for fila in range(3):
        for columna in range(3):
            if TABLERO[fila][columna] == 'X':
                pygame.draw.line(VENTANA, NEGRO, (columna * 100 + 25, fila * 100 + 25), (columna * 100 + 75, fila * 100 + 75), 3)
                pygame.draw.line(VENTANA, NEGRO, (columna * 100 + 25, fila * 100 + 75), (columna * 100 + 75, fila * 100 + 25), 3)
            elif TABLERO[fila][columna] == 'O':
                pygame.draw.circle(VENTANA, NEGRO, (columna * 100 + 50, fila * 100 + 50), 40, 3)

    pygame.display.update()

# Función para verificar el estado del juego (ganador o empate)
def verificar_estado_juego():
    ganador = None
    empate = True

    # Verificar filas
    for fila in range(3):
        if TABLERO[fila][0] == TABLERO[fila][1] == TABLERO[fila][2] and TABLERO[fila][0] != '':
            ganador = TABLERO[fila][0]
            empate = False
            break

    # Verificar columnas
    for columna in range(3):
        if TABLERO[0][columna] == TABLERO[1][columna] == TABLERO[2][columna] and TABLERO[0][columna] != '':
            ganador = TABLERO[0][columna]
            empate = False
            break

    # Verificar diagonales
    if TABLERO[0][0] == TABLERO[1][1] == TABLERO[2][2] and TABLERO[0][0] != '':
        ganador = TABLERO[0][0]
        empate = False
    elif TABLERO[1][2] == TABLERO[2][0] == TABLERO[0][2] and TABLERO[1][1] != '':
        ganador = TABLERO[1][1]
        empate = False
        ##tomar en cuenta
        
    if ganador:
        return ganador
    elif empate:
        return 'Empate'
    else:
        return None
#ciclo game
jugando = True
while jugando:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
sys.exit()
elif event.type == pygame.MOUSEBUTTONDOWN:
# Obtener posición del clic del mouse
x, y = pygame.mouse.get_pos()
fila = y // 100
columna = x // 100

# Verificar si la casilla está vacía
if TABLERO[fila][columna] == '':
    TABLERO[fila][columna] = jugador_actual
    dibujar_tablero()

    # Verificar el estado del juego
    ganador = verificar_estado_juego()
    if ganador:
        if ganador == 'Empate':
            print('¡Es un empate!')
        else:
            print(f'¡El jugador {ganador} ha ganado!')
        jugando = False
        break

        # Cambiar de jugador
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

pygame.quit()
sys.exit()
