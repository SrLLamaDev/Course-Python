def calcular_sumatoria(n):
    total = 0
    i = 1
    while i < n:
        # Patrones: (1-0), (1-2), (3-2), (3-4), (5-4), ...
        total += i - (i - 1)
        i += 1
        if i < n:
            total += i - (i + 1)
            i += 1
        if i < n:
            total += i - (i - 1)
            i += 1
        if i < n:
            total += i - (i + 1)
            i += 1
        if i < n:
            total += i - (i - 1)
            i += 1
    return total

# Leer varias entradas desde consola
try:
    while True:
        n = int(input())
        if n == 0:
            break
        # Llamar a la función y mostrar el resultado
        print(calcular_sumatoria(n))
except EOFError:
    pass
