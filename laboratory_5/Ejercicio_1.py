'''
Entrada:
8
Salida:
        1
       2 1
      4 2 1
     8 4 2 1
   16 8 4 2 1
  32 16 8 4 2 1
 64 32 16 8 4 2 1
128 64 32 16 8 4 2 1
'''

# Solicitar la cantidad de líneas
n = int(input("Ingrese el número de líneas (1-10): "))

# Generar la pirámide
for i in range(n):
    row = [2**j for j in range(i + 1)]  # Parte creciente
    row += row[-2::-1]  # Parte decreciente (sin repetir el último elemento)
    
    # Imprimir la línea sin espacios adicionales
    #print(" ".join(map(str, row)))
    print(" " * (n - i - 1) + " ".join(map(str, row)))  # Imprimir la línea con espacios iniciales
    #print(" " * (n - i - 1) + " ".join(map(str, row)), end="")  # Imprimir la línea con espacios iniciales