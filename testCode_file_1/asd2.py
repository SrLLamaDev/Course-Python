from queue import Queue

# Crear una cola
cola = Queue()
cola.put('A')
cola.put('B')
cola.put('C')

# Imprimir los elementos de la cola
print("Elementos de la cola:")
while not cola.empty():
    elemento = cola.get()
    print(elemento)

