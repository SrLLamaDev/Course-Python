import numpy as np

# Crear un array de NumPy
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Operaciones básicas
print("Suma:", np.sum(arr))
print("Media:", np.mean(arr))
print("Desviación estándar:", np.std(arr))

# Crear una matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatriz:")
print(matriz)

# Transponer la matriz
print("\nMatriz Transpuesta:")
print(matriz.T)

# Producto punto entre matrices
matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("\nProducto Punto:")
print(np.dot(matriz, matriz2))