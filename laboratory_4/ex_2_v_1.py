# Pedir al usuario que ingrese cinco números separados por espacio
lista = list(map(int, input("Ingrese números: ").split()))

# Verificar que el usuario ingresó exactamente 5 números
if len(lista) != 5:
    print("Error: Debe ingresar exactamente cinco números.")
else:
    for lista in [0,1,2,3,4]:
        print(lista)
    
    # Imprimir los resultados
    #print(f"AA = {minimo}, BB = {maximo}")
