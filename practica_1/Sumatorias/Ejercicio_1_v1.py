def generar_fibonacci(n):
    """
    Genera los primeros n números de la serie de Fibonacci modificada.
    """
    fibonacci = [1, 1]  # Los dos primeros números de Fibonacci
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci


def generar_primos(n):
    """
    Genera los primeros n números primos.
    """
    primos = []
    num = 2  # Número inicial para buscar primos
    while len(primos) < n:
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
        num += 1
    return primos


def generar_signos(n):
    """
    Genera la secuencia de signos para la serie: +, - -, + + +, - - - -, ...
    """
    signos = []
    grupo = 1
    signo_actual = 1  # Empieza con positivo (+)
    while len(signos) < n:
        signos.extend([signo_actual] * grupo)
        grupo += 1
        signo_actual *= -1  # Cambiar el signo
    return signos[:n]


def generar_serie(n):
    """
    Genera los primeros n términos de la serie S.
    """
    # Generar numeradores (Fibonacci), denominadores (primos) y signos
    numeradores = generar_fibonacci(n)
    denominadores = generar_primos(n)
    signos = generar_signos(n)

    # Calcular los términos de la serie
    serie = []
    for i in range(n):
        termino = signos[i] * (numeradores[i] / denominadores[i])
        serie.append(termino)

    return serie


# Solicitar al usuario el número de términos
try:
    n = int(input("Ingresa el número de términos (N): "))
    if n <= 0:
        print("Por favor, ingresa un número mayor que 0.")
    else:
        # Generar y mostrar la serie
        serie = generar_serie(n)
        print("Serie generada:", serie)
        print("Suma de la serie:", sum(serie))
except ValueError:
    print("Por favor, ingresa un número entero válido.")