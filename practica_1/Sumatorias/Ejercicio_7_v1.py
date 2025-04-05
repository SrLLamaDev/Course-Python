def main():
    # Leer el número de casos
    N = int(input())

    # Leer cada caso de prueba
    casos = []
    for _ in range(N):
        c = int(input())
        casos.append(c)

    # Generar la serie hasta el término 40
    serie = [0, 1, 1]
    for i in range(3, 40):
        serie.append(serie[i-1] + serie[i-2] + serie[i-3])

    # Calcular sumas acumuladas
    suma_serie = []
    acumulado = 0
    for num in serie:
        acumulado += num
        suma_serie.append(acumulado)

    # Mostrar resultados
    for c in casos:
        print(suma_serie[c - 1])

# Ejecutar
main()
