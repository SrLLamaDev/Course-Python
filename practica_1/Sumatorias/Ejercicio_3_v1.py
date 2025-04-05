def calcular_sumatoria(n, x):
    """
    Calcula la sumatoria para un caso dado de n términos y valor x.
    """
    resultado = 0
    signo = -1  # Comienza con signo negativo
    potencia = 1
    denominador = 1

    for i in range(1, n + 1):
        # Calcular el término actual
        termino = signo * (x**potencia) / denominador
        resultado += termino

        # Actualizar valores para el siguiente término
        signo *= -1  # Alternar el signo
        potencia += 1  # Incrementar la potencia de x
        denominador += i  # Actualizar el denominador acumulativo

    return resultado


# Leer la entrada
t = int(input())  # Número de casos de prueba

resultados = []
for _ in range(t):
    n, x = map(int, input().split())
    # Calcular la sumatoria para cada caso
    resultado = calcular_sumatoria(n, x)
    resultados.append(f"{resultado:.4f}")

# Imprimir los resultados
print("\n".join(resultados))