'''
Calculo sobre el triangulo
a) las longitudes de su lados
b) los ángulos de sus esquinas
c) el perímetro
d) el área
-------------------------------------------------
Calculo de lados: con la formula de la distancia euclidiana 
Calculo de los angulos: con la ley de los cosenos
Calculo del perimetro: suma de los lados
Calculo del area: se usa la formula de Herón
'''
import math

# Función para calcular la distancia entre dos puntos
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Función para calcular el ángulo usando la Ley de los Cosenos
def angulo(a, b, c):
    return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

# Entrada de los vértices
x1, y1, x2, y2, x3, y3 = map(float, input("Ingrese los tres vértices v1, v2 y v3 (x1 y1 x2 y2 x3 y3): ").split())

# a) Calcular las longitudes de los lados
lado_a = distancia(x2, y2, x3, y3)  # Entre V2 y V3
lado_b = distancia(x1, y1, x3, y3)  # Entre V1 y V3
lado_c = distancia(x1, y1, x2, y2)  # Entre V1 y V2

# b) Calcular los ángulos
angulo_A = angulo(lado_a, lado_b, lado_c)  # Ángulo en V1
angulo_B = angulo(lado_b, lado_c, lado_a)  # Ángulo en V2
angulo_C = angulo(lado_c, lado_a, lado_b)  # Ángulo en V3

# c) Calcular el perímetro
perimetro = lado_a + lado_b + lado_c

# d) Calcular el área usando la fórmula de Herón
s = perimetro / 2
area = math.sqrt(s * (s - lado_a) * (s - lado_b) * (s - lado_c))

# Imprimir resultados
print(f"Longitud de los lados = {lado_a:.4f} {lado_b:.4f} {lado_c:.4f}")
print(f"Ángulos de las esquinas = {angulo_A:.4f} {angulo_B:.4f} {angulo_C:.4f}")
print(f"Perímetro = {perimetro:.4f}")
print(f"Área = {area:.4f}")
