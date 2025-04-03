def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generar lista de primos entre 2 y 1000
primos = [n for n in range(2, 1001) if es_primo(n)]

# Imprimir encabezado
print("Los primeros 1000 números primos son:")

# Imprimir los primos con 10 números por línea
for i in range(0, len(primos), 10):
    print(" ".join(map(str, primos[i:i+10])))
