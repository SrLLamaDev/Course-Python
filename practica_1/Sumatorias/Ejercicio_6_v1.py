def is_prime(n):
    """Función para verificar si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """Generador de números primos a partir de 2."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def main():
    N = int(input().strip())
    suma = 0
    prime_gen = generate_primes()
    # Se suman los primeros N términos alternando el signo
    for i in range(N):
        p = next(prime_gen)
        # Se asigna signo positivo a términos en posición par (0,2,4,...) y negativo a posición impar (1,3,5,...)
        signo = 1 if i % 2 == 0 else -1
        suma += signo * p
    print(suma)

if __name__ == "__main__":
    main()
