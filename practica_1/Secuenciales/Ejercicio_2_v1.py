# Entrada de datos
P, r, t = map(float, input().split())

# Cálculo del monto total a pagar
M = P + (P * (r / 100) * t)

# Salida del resultado
print(M)
