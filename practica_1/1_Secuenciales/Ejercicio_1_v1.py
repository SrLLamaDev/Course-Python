'''
Dado un numero entero N expresado en segundos, transformar en horas minutos y segundos,
en el siguiente formato, HH : MM : SS
'''

'''
Entrada de datos
7400
Ejemplo de salida
02:03:20
'''
#realzia el codigo
# Definicion de variables
N = int(input('Ingrese el tiempo en segundos: ')) # tiempo en segundos
horas = 0 # horas
minutos = 0 # minutos  
segundos = 0 # segundos
# Proceso
horas = N // 3600 # division entera de N entre 3600
minutos = (N % 3600) // 60 # division entera de N entre 60
segundos = N % 60 # resto de la division de N entre 60
# Salida de datos
print(f'{horas:02d}:{minutos:02d}:{segundos:02d}') # imprime la hora en formato HH:MM:SS    