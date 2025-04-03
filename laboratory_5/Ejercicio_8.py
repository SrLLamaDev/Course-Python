def cantor_term(n):
    # Determinar en qué diagonal se encuentra el término
    diagonal = 1
    while n > (diagonal * (diagonal + 1)) // 2:
        diagonal += 1
    
    # Determinar la posición dentro de la diagonal
    index_in_diagonal = n - (diagonal * (diagonal - 1)) // 2
    
    # Calcular numerador y denominador
    if diagonal % 2 == 0:
        numerador = index_in_diagonal
        denominador = diagonal - index_in_diagonal + 1
    else:
        numerador = diagonal - index_in_diagonal + 1
        denominador = index_in_diagonal
    
    return f"{numerador}/{denominador}"

# Leer múltiples valores de entrada
entradas = [int(input()) for _ in range(3)]  # Ajusta según la cantidad de valores de entrada

# Imprimir la salida correspondiente a cada entrada
for n in entradas:
    print(cantor_term(n))