import math

# Función para generar los primeros n términos de la sucesión de Fibonacci
def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Función para generar los primeros n números primos
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

# Función para calcular la suma de la serie
def calcular_serie(n):
    fibs = fibonacci(n)
    primes = primos(n)
    suma = 0
    for i in range(n):
        numerador = math.factorial(fibs[i])
        denominador = primes[i]
        suma += numerador / denominador
    return suma

# Ejemplo de uso
n = int(input("Introduce el número de términos a calcular: "))
resultado = calcular_serie(n)
print(f"La suma de los primeros {n} términos es: {resultado}")
