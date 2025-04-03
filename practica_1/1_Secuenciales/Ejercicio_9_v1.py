'''
Dada una temperatura en grados Celsius C, imprimir en:
1. Fahrenheit
2. Kelvin
3. Rankine
4. R´eaumur
'''
'''
Entrada de datos:
25
Salida de datos:
77 °F
298.15 °K
532.67 °R
20 °Re
'''
# Definicion de variables
C = float(input('Ingrese la temperatura en grados Celsius: ')) # temperatura en grados Celsius
F = 0 # temperatura en grados Fahrenheit
K = 0 # temperatura en grados Kelvin
R = 0 # temperatura en grados Rankine
Re = 0 # temperatura en grados Reaumur
# Proceso
F = (C * 9/5) + 32 # conversion de Celsius a Fahrenheit
K = C + 273.15 # conversion de Celsius a Kelvin
R = (C + 273.15) * 9/5 # conversion de Celsius a Rankine
Re = C * 4/5 # conversion de Celsius a Reaumur
# Salida de datos
print(f'{F:.2f} °F') # imprime la temperatura en Fahrenheit
print(f'{K:.2f} °K')
print(f'{R:.2f} °R')
print(f'{Re:.2f} °Re')
