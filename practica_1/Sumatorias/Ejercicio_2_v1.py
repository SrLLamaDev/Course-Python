from math import factorial  # Para calcular los factoriales

def generar_sumatoria(n, x):
    """
    Genera la sumatoria de N términos de acuerdo con la fórmula dada.
    """
    sumatoria = []  # Para almacenar los términos como cadenas para impresión
    resultado = 0  # Resultado acumulado de la sumatoria

    for i in range(1, n + 1):
        # Determinar la posición cíclica del exponente y el denominador
        exponente = (i % 3) if (i % 3) != 0 else 3
        denominador = (i % 4) if (i % 4) != 0 else 4

        # Calcular el término
        numerador = x ** exponente
        termino = numerador / factorial(denominador)

        # Alternar signos
        if (i % 2) == 0:
            termino = -termino
            sumatoria.append(f"- {numerador}/{factorial(denominador)}")
        else:
            sumatoria.append(f"+ {numerador}/{factorial(denominador)}")

        # Acumular el resultado
        resultado += termino

    # Preparar la salida
    sumatoria_string = " ".join(sumatoria).lstrip("+ ")  # Eliminar el primer signo "+"
    return sumatoria_string, resultado


# Entrada del usuario
n = int(input())
x = int(input())

# Generar la sumatoria
if 1 <= n <= 100 and 1 <= x <= 10:
    sumatoria_string, resultado = generar_sumatoria(n, x)

    # Imprimir los resultados
    print("Sumatoria Generada:")
    print(sumatoria_string)
else:
    print("Los valores de entrada no cumplen con las restricciones.")