import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def next_prime(start):
    # Generador de números primos a partir de 'start'
    num = start
    while True:
        if is_prime(num):
            yield num
        num += 1

def main():
    # Se leen los valores de entrada: N términos y X
    entrada = input().split()
    if len(entrada) < 2:
        return
    N = int(entrada[0])
    X = int(entrada[1])
    
    total = 0.0
    term_count = 0
    grupo = 1
    prime_gen = next_prime(2)
    
    # Se generan términos en grupos: grupo 1 tiene 1 término, grupo 2 tiene 2, etc.
    while term_count < N:
        # El denominador para los términos del grupo actual es factorial(X + grupo)
        denominador = math.factorial(X + grupo)
        for i in range(1, grupo + 1):
            if term_count >= N:
                break
            p = next(prime_gen)  # siguiente primo
            # Para el grupo 1, el único término es positivo.
            # Para los grupos a partir del 2, se asigna signo negativo al primer término y se alterna.
            if grupo == 1:
                signo = 1
            else:
                signo = -1 if i % 2 != 0 else 1
            
            termino = signo * math.factorial(p) / denominador
            total += termino
            term_count += 1
    # Se imprime el resultado con 2 decimales.
    print(f"{total:.2f}")

if __name__ == '__main__':
    main()
