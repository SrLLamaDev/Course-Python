import heapq

def union(cola1, cola2):
    result = []
    for element in cola1 + cola2:
        heapq.heappush(result, element)
    return result

def interseccion(cola1, cola2):
    result = []
    for element in cola1:
        if element in cola2:
            heapq.heappush(result, element)
    return result

# Colas de entrada
colaA = ['a', 'b', 'c']
colaB = ['a', 'd']

# Unión de las colas
union_result = union(colaA, colaB)
print("Unión: ", union_result)

# Intersección de las colas
interseccion_result = interseccion(colaA, colaB)
print("Intersección: ", interseccion_result)
