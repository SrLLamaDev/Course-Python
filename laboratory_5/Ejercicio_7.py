'''
la media y la desviacion estandar de 10 numeros
Entrada:
10 20 30 40 50 60 70 80 90 100
Salida:
La media es 55.00
La desviación estándar es 28.86607
'''

import statistics

def main():
    # Solicitar al usuario que ingrese 10 números separados por espacio
    numeros = list(map(float, input("Ingrese diez números: ").split()))
    
    # Verificar que se ingresaron exactamente 10 números
    if len(numeros) != 10:
        print("Por favor, ingrese exactamente 10 números.")
        return
    
    # Calcular la media
    media = statistics.mean(numeros)
    
    # Calcular la desviación estándar
    desviacion = statistics.stdev(numeros)
    
    # Mostrar los resultados
    print(f"La media es {media:.2f}")
    print(f"La desviación estándar es {desviacion:.5f}")

if __name__ == "__main__":
    main()
