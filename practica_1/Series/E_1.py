def generar_serie(n):
    serie = []
    bloque = 1
    while len(serie) < n:
        for i in range(1, bloque + 1):
            if len(serie) >= n:
                break
            serie.append(i)
        bloque += 1
    return serie

# Solicitar el valor de N al usuario
try:
    n = int(input("Ingrese la cantidad de términos de la serie que desea generar: "))
    if n <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        resultado = generar_serie(n)
        print("Serie generada:")
        print(resultado)
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")
