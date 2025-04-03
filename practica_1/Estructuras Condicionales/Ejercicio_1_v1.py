'''
Descripcion: 
Dado 2 intervalos, calcule el intervalo que corresponde a su interseccion o indica si esta vacıo.
Entrada: 
La entrada consiste de cuatro numeros enteros 
a1, b1, a2, b2, que representan los intervalos [a1, b1] y [a2, b2]. Asuma que a1 ≤ b1 y a2 ≤ b2
Salida: Imprima [] si la interseccion esta vacıa o [x, y] si la interseccion no esta vacıa.
'''
'''
Entrada de datos:
20 30 10 40
Salida de datos:
[20, 30]
'''
# Definicion de variables
a1, b1, a2, b2 = map(int, input('Ingrese los intervalos: ').split()) # intervalos [a1, b1] y [a2, b2]
# Proceso
if a1 <= b1 and a2 <= b2: # verifica que los intervalos sean validos
    if a1 > b2 or a2 > b1: # verifica si la interseccion esta vacia
        print('[]') # imprime [] si la interseccion esta vacia
    else: # si la interseccion no esta vacia
        x = max(a1, a2) # obtiene el valor maximo de a1 y a2
        y = min(b1, b2) # obtiene el valor minimo de b1 y b2
        print(f'[{x}, {y}]') # imprime el intervalo de interseccion [x, y]
        
