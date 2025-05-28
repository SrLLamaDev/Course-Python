def encender_bit(n, x):
    # Calcula el nuevo número encendiendo el bit 'x'
    resultado = n | (1 << (x - 1))
    return resultado

def main():
    n = int(input("Ingresa el valor de n: "))
    x = int(input("Ingresa el número de bit a encender (1 a 8): "))

    resultado = encender_bit(n, x)
    print("Resultado en decimal:", resultado)

if __name__ == "__main__":
    main()
