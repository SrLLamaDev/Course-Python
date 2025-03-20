import numpy as np
import matplotlib.pyplot as plt

# Rango de valores para N
N = np.linspace(1, 1000, 400)  # 400 puntos entre 1 y 1000

# Definir las funciones de complejidad
O_N = N            # O(N)
O_sqrtN = np.sqrt(N)  # O(√N)

# Crear la gráfica
plt.figure(figsize=(8, 5))
plt.plot(N, O_N, label=r'$O(N)$', color='r', linewidth=2)
plt.plot(N, O_sqrtN, label=r'$O(\sqrt{N})$', color='b', linestyle='--', linewidth=2)

# Etiquetas y título
plt.xlabel("N")
plt.ylabel("Crecimiento de la función")
plt.title("Comparación de O(N) y O(√N)")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
