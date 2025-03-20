import numpy as np
import matplotlib.pyplot as plt

# Rango de valores para N (evitando log(0))
N = np.linspace(1, 1000, 400)  # 400 puntos entre 1 y 1000
O_logN = np.log(N)             # O(log N)
O_logN3 = 3 * np.log(N)        # O(log(N^3)) = 3 * log(N)

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(N, O_logN, label=r'$O(\log N)$', color='r', linestyle='--', linewidth=2)
plt.plot(N, O_logN3, label=r'$O(\log N^3) = 3\log N$', color='b', linewidth=2)

# Etiquetas y título
plt.xlabel("N")
plt.ylabel("Crecimiento de la función")
plt.title("Comparación de O(log N) y O(log N^3)")
plt.legend()
plt.grid(True)
plt.show()
