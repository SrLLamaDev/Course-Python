def maximum_money(M, C, prices):
    dp = [0] * (M + 1)  # Arreglo para almacenar los valores máximos posibles de dinero
    x = 5
    for i in range(C):
        models = prices[i][0]  # Número de modelos diferentes
        models_prices = prices[i][1:]  # Precios de los modelos de la prenda

        for j in range(M, 0, -1):
            for k in range(models):
                if models_prices[k] <= j:
                    dp[j] = max(dp[j], dp[j - models_prices[k]] + models_prices[k])

        
    if dp[M] <= x :
      
        return "no solution"
               
    else:
        return dp[M]

# Lectura de la entrada
num_cases = int(input())

for _ in range(num_cases):
    M, C = map(int, input().split())
    prices = []

    for _ in range(C):
        prices.append(list(map(int, input().split())))

    result = maximum_money(M, C, prices)
    print(result)
