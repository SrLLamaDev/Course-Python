'''
Entrada: numeros flotantes 
D es la demanda, S es el costo de cada pedido y H es el costo de almacenamiento por a˜no, en ese orden respectivamente.
Salida: Q = raiz cuadrada de 2DS/H
'''
'''
Ejemplo entrada:
2000 1.5 0.5
Ejemplo salida:

'''
#Entrada de datos
D, S, H = map(float, input('Entrada: ').split()) # demanda, costo de cada pedido y costo de almacenamiento por año
#proceso
Q = (2 * D * S )/ H # raiz cuadrada de 2DS/H
Q = Q ** 0.5 # raiz cuadrada de Q
#Salida de datos
print(f'Salida: {Q:.2f}') # imprime la cantidad economica de pedido
