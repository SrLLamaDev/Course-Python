import math

def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def generar_serie(n):
    fib_nums = fibonacci(n)
    
    # Construimos los denominadores de acuerdo al patrón de la imagen
    denominadores = []
    i = 1
    while len(denominadores) < n:
        if i == 1:
            denominadores += [1, 2]
        elif i == 2:
            denominadores.append(2)
        elif i == 3:
            denominadores += [3, 3, 3]
        elif i == 4:
            denominadores += [4, 4]
        else:
            denominadores.append(i)
        i += 1

    suma_total = 0
    print("Términos de la serie:")

    for i in range(n):
        num = fib_nums[i]
        den = denominadores[i]
        valor = math.factorial(num) / den
        print(f"{num}!/{den} = {valor}")
        suma_total += valor

    print(f"\nSuma total de los primeros {n} términos: {suma_total}")

# --- Entrada del usuario ---
try:
    cantidad = int(input("Ingrese: "))
    generar_serie(cantidad)
except ValueError:
    print("Por favor, ingresa un número entero válido.")
