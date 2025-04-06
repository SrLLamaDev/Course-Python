def generar_serie_factorial(n):
    serie = []
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        serie.append(factorial)
    return serie

# Pedir al usuario el valor de n
try:
    n = int(input("Ingrese la cantidad de términos de la serie factorial que desea generar: "))
    if n <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        resultado = generar_serie_factorial(n)
        print("Serie generada:")
        print(resultado)
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")
