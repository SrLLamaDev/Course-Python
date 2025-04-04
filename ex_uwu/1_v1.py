import math

def calcular_sumatoria(n, x):
    suma1 = sum(2 / k for k in range(1, n + 1))
    suma2 = sum(((-1) ** i / math.factorial(2 + i)) * (x ** (2 + i)) for i in range(1, n + 1))
    return suma1 + suma2

# Solicitar datos al usuario
n = int(input("Ingrese el valor de n: "))
x = float(input("Ingrese el valor de x: "))

# Calcular la sumatoria
resultado = calcular_sumatoria(n, x)

# Mostrar resultado
print("El resultado de la sumatoria es:", resultado)
