def generar_serie(n):
    serie = [1, 2, 3, 4]
    while len(serie) < n:
        nuevo_valor = sum(serie[-4:])  # suma de los últimos 4 elementos
        serie.append(nuevo_valor)
    return serie[:n]  # en caso de que n < 4

# Pedir al usuario el valor de n
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
