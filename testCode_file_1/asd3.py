from queue import Queue

# Definir las colas A y B
colaA = Queue()
colaA.put('a')
colaA.put('b')
colaA.put('c')

colaB = Queue()
colaB.put('a')
colaB.put('d')

# Crear una cola para la unión
colaUnion = Queue()

# Crear una cola para la intersección
colaInterseccion = Queue()

# Copiar colaA a colaUnion
while not colaA.empty():
    elemento = colaA.get()
    colaUnion.put(elemento)
    colaInterseccion.put(elemento)
'''
# Copiar colaB a colaUnion y colaInterseccion, evitando duplicados
while not colaB.empty():
    elemento = colaB.get()
    if elemento not in colaUnion.queue:
        colaUnion.put(elemento)
    if elemento in colaInterseccion.queue:
        colaInterseccion.put(elemento)
'''
while not colaB.empty():
    elemento = colaB.get()
    if elemento not in colaUnion.queue:
        colaUnion.put(elemento)
    if elemento in colaA.queue:
        colaInterseccion.put(elemento)
print("Union:")
print("A U B:", list(colaUnion.queue))
print("Interseccion:")
print("A ∩ B", list(colaInterseccion.queue))
##print("Cola de Unión: ", list(colaUnion.queue))
##print("Cola de Intersección: ", list(colaInterseccion.queue))
