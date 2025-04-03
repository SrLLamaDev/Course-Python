import heapq

# Definir las colas
colaA = ['a', 'b', 'c']
colaB = ['a', 'd']

# Obtener la unión usando una cola de prioridad
union = list(set(colaA) | set(colaB))
cola_union = []
for elemento in union:
    heapq.heappush(cola_union, elemento)

# Obtener la intersección usando una cola de prioridad
interseccion = list(set(colaA) & set(colaB))
cola_interseccion = []
for elemento in interseccion:
    heapq.heappush(cola_interseccion, elemento)

# Imprimir la cola de unión
print("Cola de Unión:")
while cola_union:
    elemento = heapq.heappop(cola_union)
    print(elemento)

# Imprimir la cola de intersección
print("Cola de Intersección:")
while cola_interseccion:
    elemento = heapq.heappop(cola_interseccion)
    print(elemento)
