def contar_fibonacci(a, b):
    fib = [0, 1]  # Inicializa la serie con f0 = 0 y f1 = 1
    count = 0

    # Generar la serie de Fibonacci hasta que supere 'b'
    while fib[-1] <= b:
        fib.append(fib[-1] + fib[-2])

    # Contar los números de Fibonacci en el rango [a, b]
    for num in fib:
        if a <= num <= b:
            count += 1

    print(count)

# Leer múltiples pares de entrada
while True:
    try:
        a, b = map(int, input().split())  # Leer valores de entrada
        contar_fibonacci(a, b)
    except EOFError:  # Manejo del fin de entrada
        break
