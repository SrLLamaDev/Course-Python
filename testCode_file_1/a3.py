def maximum_money(M, C, prices):
    dp = [False] * (M + 1)  # Arreglo para almacenar los valores máximos posibles de dinero
    dp[0] = True

    for i in range(C):
        models = prices[i][0]  # Número de modelos diferentes
        models_prices = prices[i][1:]  # Precios de los modelos de la prenda

        for k in range(models):
            for j in range(M, models_prices[k] - 1, -1):
                if dp[j - models_prices[k]]:
                    dp[j] = True

    for i in range(M, -1, -1):
        if dp[i]:
            return i

    return "no solution"

# Lectura de la entrada
num_cases = int(input())

for _ in range(num_cases):
    M, C = map(int, input().split())
    prices = []

    for _ in range(C):
        prices.append(list(map(int, input().split())))

    result = maximum_money(M, C, prices)
    print(result)
