import math

def factorial(n):
    """Calcula el factorial de un número."""
    return 1 if n == 0 else n * factorial(n - 1)

def taylor_sin(x, n):
    """Calcula sin(x) usando la serie de Taylor hasta n términos."""
    sin_x = sum(((-1)**k * (x**(2*k+1)) / factorial(2*k+1)) for k in range(n+1))
    return sin_x

def taylor_cos(x, n):
    """Calcula cos(x) usando la serie de Taylor hasta n términos."""
    cos_x = sum(((-1)**k * (x**(2*k)) / factorial(2*k)) for k in range(n+1))
    return cos_x

def taylor_exp(x, n):
    """Calcula e^x usando la serie de Taylor hasta n términos."""
    exp_x = sum((x**k) / factorial(k) for k in range(n+1))
    return exp_x

# Leer el valor de entrada
x = float(input().strip())

# Imprimir encabezado
print(f"n    sin({x})       cos({x})       e^{x}")
print("--   -------------  -------------  -------------")

# Calcular e imprimir valores para n = 0, 1, 2, ...
for n in range(15):  # Puedes ajustar el número de términos
    sin_x = taylor_sin(x, n)
    cos_x = taylor_cos(x, n)
    exp_x = taylor_exp(x, n)
    print(f"{n:02}   {sin_x:.11f}  {cos_x:.11f}  {exp_x:.11f}")
