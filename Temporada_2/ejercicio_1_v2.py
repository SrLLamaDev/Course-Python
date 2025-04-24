import math

def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def primos(n):
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def calcular_serie_y_mostrar(n):
    fibs = fibonacci(n)
    primes = primos(n)
    suma = 0
    partes = []

    for i in range(n):
        num = fibs[i]
        den = primes[i]
        partes.append(f"{num}!/{den}")
        suma += math.factorial(num) / den

    formula = " + ".join(partes)
    print(f"Serie: {formula}")
    print(f"Suma total: {suma}")

# Solicita al usuario un número n
try:
    n = int(input("Ingrese el número de términos de la serie: "))
    if n <= 0:
        print("Por favor ingrese un número positivo.")
    else:
        calcular_serie_y_mostrar(n)
except ValueError:
    print("Entrada no válida. Por favor ingrese un número entero.")
