def fibonacci_series(n):
    if n == 0:
        print(0)
        return
    
    fib = [0, 1]  # Inicializa la serie con f0 = 0 y f1 = 1
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])  # Calcula el siguiente número en la serie

    print(" ".join(map(str, fib)))  # Imprime la serie en una línea

# Leer la entrada y procesar cada caso
while True:
    try:
        n = int(input().strip())  # Leer número
        fibonacci_series(n)
    except EOFError:  # Manejo de fin de entrada
        break
        