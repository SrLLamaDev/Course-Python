#Calcula la longitud del lado c y os angulos A y B utilizando la Ley de los Cosenos.
import math

# Solicitar entrada al usuario
a = float(input("a (cm): "))
b = float(input("b (cm): "))
C = float(input("C (grados): "))

# Convertir C de grados a radianes
C_rad = math.radians(C)

# a) Calcular la longitud de c usando la Ley de los Cosenos
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C_rad))

# b) Calcular los ángulos A y B usando la Ley de los Cosenos
A_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
B_rad = math.acos((a**2 + c**2 - b**2) / (2 * a * c))

# Convertir los ángulos de radianes a grados
A = math.degrees(A_rad)
B = math.degrees(B_rad)

# c) Calcular la suma de los ángulos
suma_angulos = A + B + C

# Imprimir los resultados
print(f"c = {c:.4f}")
print(f"A = {A:.4f}")
print(f"B = {B:.4f}")
print(f"Suma de ángulos = {suma_angulos:.4f}")
