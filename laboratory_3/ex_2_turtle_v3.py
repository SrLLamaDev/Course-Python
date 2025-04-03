import matplotlib.pyplot as plt
import numpy as np

def dibujar_flecha(ax, x_ini, y_ini, x_fin, y_fin, margen=0.1):
    # Calcular dirección de la flecha
    dx = x_fin - x_ini
    dy = y_fin - y_ini
    norm = np.sqrt(dx**2 + dy**2)
    
    # Ajustar puntos de inicio y fin con margen
    x_ini_adj = x_ini + margen * dx
    y_ini_adj = y_ini + margen * dy
    x_fin_adj = x_fin - margen * dx
    y_fin_adj = y_fin - margen * dy
    
    # Dibujar la línea de la flecha
    ax.plot([x_ini_adj, x_fin_adj], [y_ini_adj, y_fin_adj], 'k-', linewidth=2)
    
    # Coordenadas del triángulo (cabeza de la flecha)
    head_x = [x_fin_adj, x_fin_adj - 0.05 * (dx - dy), x_fin_adj - 0.05 * (dx + dy)]
    head_y = [y_fin_adj, y_fin_adj - 0.05 * (dy + dx), y_fin_adj - 0.05 * (dy - dx)]
    
    # Dibujar la cabeza de la flecha
    ax.fill(head_x, head_y, 'k')

def dibujar_cuadrado():
    fig, ax = plt.subplots()
    
    # Dibujar cuatro flechas formando un cuadrado con margen
    dibujar_flecha(ax, 0, 0, 1, 0)  # Abajo
    dibujar_flecha(ax, 1, 0, 1, 1)  # Derecha
    dibujar_flecha(ax, 1, 1, 0, 1)  # Arriba
    dibujar_flecha(ax, 0, 1, 0, 0)  # Izquierda
    
    # Ajustar límites y ocultar ejes
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.show()

dibujar_cuadrado()
