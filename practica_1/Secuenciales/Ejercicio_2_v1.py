'''
Para el c´alculo del cobro de un prestamo, se pide que para la cuantificacion del pago se tome
en cuenta el dinero prestado, el interes anual y los a˜nos en los que la deuda se cancela.
'''
'''
Entrada de datos
500 10 4
Ejemplo de salida
5000.0
'''

# Entrada de datos
P, r, t = map(float, input().split())

# Cálculo del monto total a pagar
M = P + (P * (r / 100) * t)

# Salida del resultado
print(M)
