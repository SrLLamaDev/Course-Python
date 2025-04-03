from itertools import combinations

def generar_combinaciones():
    numeros = list(range(1, 8))  # Números del 1 al 7
    comb = list(combinations(numeros, 2))  # Generar todas las combinaciones de 2
    
    # Imprimir combinaciones
    for c in comb:
        print(c[0], c[1])
    
    # Imprimir el número total de combinaciones
    print(f"\nEl número total de todas las combinaciones es {len(comb)}")

# Ejecutar la función
generar_combinaciones()