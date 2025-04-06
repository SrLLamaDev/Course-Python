def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generar_serie(n):
    serie = []
    fib1, fib2 = 0, 1  # primeros números de Fibonacci
    num = 2  # para generar primos

    for i in range(n):
        if i % 2 == 0:
            # posición par: número de Fibonacci
            serie.append(fib1)
            fib1, fib2 = fib2, fib1 + fib2
        else:
            # posición impar: número primo
            while not es_primo(num):
                num += 1
            serie.append(num)
            num += 1

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


