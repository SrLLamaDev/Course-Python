import heapq
def union(cola1, cola2):
    resultado = []
    for elemento in cola1 + cola2:
        if elemento not in resultado:
            resultado.append(elemento)
    heapq.heapify(resultado)
    return resultado
def interseccion(cola1, cola2):
    resultado = []
    for elemento in cola1:
        if elemento in cola2:
            resultado.append(elemento)
    heapq.heapify(resultado)
    return resultado
##print("     Cola de Prioridad:      ")
print ("----------------------------")
print ("        COLA:               ")
print ("----------------------------")
cola1 = ['a', 'b', 'c']
print ("Cola 1: ",cola1)
cola2 = ['a', 'd']
print ("Cola 2: ",cola2)
print ("----------------------------")
print ("        RESULTADO:          ")
print ("----------------------------")
union_resultado = union(cola1, cola2)
##print("Unión:", union_resultado)
interseccion_resultado = interseccion(cola1, cola2)
##print("Intersección:", interseccion_resultado)
print("Union:")
print("A U B:", union_resultado)
print("Interseccion:")
print("A ∩ B:", interseccion_resultado)
