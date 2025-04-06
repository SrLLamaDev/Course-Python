def generar_serie(n):
    serie = [1]
    impar = 1  # el primer incremento fue 2, siguiente impar será 3
    saltos = [2, 3, 5, 7]  # primeros saltos
    i = 1  # índice actual en la serie

    while len(serie) < n:
        # Si terminamos una secuencia, agregamos un +1 y reiniciamos saltos
        if len(saltos) == 0:
            serie.append(serie[-1] + 1)
            # Reiniciamos el patrón con mayores impares
            impar += 2
            saltos = [impar, impar + 2, impar + 4]
        else:
            salto = saltos.pop(0)
            serie.append(serie[-1] + salto)
    
    return serie

try:
    n = int(input("Ingrese:"))
    if n <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        resultado = print(generar_serie(n))
        print("Serie generada:")
        print(resultado)
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejemplo: mostrar los primeros 20 términos

