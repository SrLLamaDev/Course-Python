def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_primos(n):
    """Encuentra el enésimo número primo en la serie de Fibonacci."""
    fib = [0, 1]  # Serie de Fibonacci inicial
    primos_fib = []  # Lista de números primos en Fibonacci

    while len(primos_fib) < n:
        fib.append(fib[-1] + fib[-2])  # Generar el siguiente Fibonacci
        if es_primo(fib[-1]):  # Verificar si es primo
            primos_fib.append(fib[-1])

    return primos_fib[n - 1]  # Devolver el enésimo primo en Fibonacci

# Leer múltiples entradas y procesar cada una
while True:
    try:
        k = int(input().strip())  # Leer el valor de entrada
        print(fibonacci_primos(k))
    except EOFError:  # Manejo del fin de entrada
        break
