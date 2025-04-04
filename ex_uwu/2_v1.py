def generar_sucesion(n):
    secuencia = []
    for i in range(n):
        # Calcular el índice de grupo (comenzando en 1)
        k = (i // 3) + 1
        
        # Posición dentro del grupo (0, 1 o 2)
        pos = i % 3
        
        if pos == 0:
            valor = 2 + k
        elif pos == 1:
            valor = 1 + k
        else:  # pos == 2
            valor = k
        
        secuencia.append(valor)
    
    return secuencia

# Ejemplo: generar los primeros 15 términos
n = 15
resultado = generar_sucesion(n)
print(resultado)
