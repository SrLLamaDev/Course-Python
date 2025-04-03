'''
Si tiene que llegar a X metros de distancia y le quedan T minutos
'''
'''
Entrada de datos:
2400 10
Salida de datos:
4 m/s
'''
# Entrada de datos
x, t = map(float, input().split())
# Proceso
v= x / (t * 60) # Velocidad en m/s
# Salida de datos
print(f'{v} m/s') # Salida de la velocidad en m/s
