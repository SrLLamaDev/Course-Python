###
cantidad = int(input("Ingrese la cantidad de artículos: "))
precio_unitario = float(input("Ingrese el precio unitario del articulo: "))

if cantidad == 1:
    total=precio_unitario*cantidad
    descuento = 0.10*total
    precio_final = precio_unitario-descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Precio final a pagar: ${precio_final:.2f}")
elif 1 < cantidad < 5:
    total=precio_unitario*cantidad
    descuento = 0.20*total
    precio_final = total-descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Precio final a pagar: ${precio_final:.2f}")
else:
    total=precio_unitario*cantidad
    descuento = 0.30*total
    precio_final = total-descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Precio final a pagar: ${precio_final:.2f}")
