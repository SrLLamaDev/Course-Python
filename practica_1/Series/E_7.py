def generar_serie(n):
    serie = []
    par = 2
    fib = [0, 1]
    
    for i in range(n):
        if i % 2 == 0:
            # Posiciones pares: número par creciente
            serie.append(par)
            par += 2
        else:
            # Posiciones impares: serie de Fibonacci
            if len(fib) < (i // 2 + 2):
                fib.append(fib[-1] + fib[-2])
            serie.append(fib[i // 2])
    
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


