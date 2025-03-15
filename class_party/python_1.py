def calcular_descuento(cantidad, precio_unitario):
    if cantidad == 1:
        descuento = 0.10
    elif 1 < cantidad < 5:
        descuento = 0.20
    else:
        descuento = 0.30

    precio_total = cantidad * precio_unitario
    descuento_aplicado = precio_total * descuento
    precio_final = precio_total - descuento_aplicado

    return precio_final, descuento_aplicado

# Ejemplo de uso
cantidad = int(input("Ingrese la cantidad de artículos: "))
precio_unitario = float(input("Ingrese el precio unitario del articulo: "))

precio_final, descuento_aplicado = calcular_descuento(cantidad, precio_unitario)

print(f"Descuento aplicado: ${descuento_aplicado:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")
