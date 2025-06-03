def ejercicio1():
    entrada = input("Ingrese números enteros, la entrada finaliza si es 0: ")
    numeros = list(map(int, entrada.split()))

    # Elimina el último número si es cero
    if numeros[-1] == 0:
        numeros = numeros[:-1]

    positivos = sum(1 for n in numeros if n > 0)
    negativos = sum(1 for n in numeros if n < 0)
    suma_total = sum(numeros)

    if len(numeros) > 0:
        promedio = suma_total / len(numeros)
    else:
        promedio = 0.0

    print(f"El número de positivos es {positivos}")
    print(f"La cantidad de negativos es {negativos}")
    print(f"La suma total es {suma_total:.1f}")
    print(f"El promedio es {promedio:.2f}")

# Para ejecutarlo:
ejercicio1()