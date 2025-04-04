def reemplazar_decenas(numeros):
   
    resultado = numeros[:]  

    def reemplaza_decena(num, nueva_decena):

        parte_superior = num // 100
        unidad = num % 10
        
        return parte_superior * 100 + nueva_decena * 10 + unidad

    N = len(numeros)
    for i in range(N):
        if numeros[i] >= 10:
            decena = (numeros[i] // 10) % 10
            siguiente = (i + 1) % N
            if resultado[siguiente] >= 10:
                resultado[siguiente] = reemplaza_decena(resultado[siguiente], decena)
    
    return resultado

if __name__ == "__main__":
    numeros = [4568, 746, 35, 5, 6575, 345, 657, 57]
    
    print("Entrada:")
    print(" ".join(map(str, numeros)))
    
    resultado = reemplazar_decenas(numeros)
    
    print("\nResultado:")
    orden_transformacion = resultado[1:] + resultado[:1]
    print(" ".join(map(str, orden_transformacion)))
