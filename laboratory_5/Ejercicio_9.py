def calcular_pagos(monto_prestamo, anos):
    print("Tasa de interés    Pago mensual    Pago total")
    print("-------------------------------------------")
    
    tasa = 5.0
    while tasa <= 8.0:
        tasa_mensual = (tasa / 100) / 12
        meses = anos * 12
        
        pago_mensual = (monto_prestamo * tasa_mensual) / (1 - (1 + tasa_mensual) ** -meses)
        pago_total = pago_mensual * meses
        
        print(f"{tasa:.3f}%           {pago_mensual:.2f}        {pago_total:.2f}")
        
        tasa += 0.125  # Incremento de 1/8%

# Entrada del usuario
monto_prestamo = float(input("Monto del préstamo: "))
anos = int(input("Cantidad de años: "))

# Calcular y mostrar pagos
calcular_pagos(monto_prestamo, anos)