import datetime

def procesar_venta(inventario):
    carrito = {}
    print("\n--- NUEVA VENTA ---")
    
    while True:
        codigo = input("Codigo del producto (o '0' para pagar): ").strip().upper()
        
        if codigo == '0':
            break
            
        if codigo not in inventario:
            print("Ese producto no existe")
            continue
            
        try:
            cantidad = int(input(f"Cuantas unidades de {inventario[codigo]['nombre']}?: "))
            
            if cantidad <= 0:
                print("Pon una cantidad mayor a 0")
                continue
                
            stock_disponible = inventario[codigo]["stock"]
            cantidad_en_carrito = carrito.get(codigo, 0)
            
            if (cantidad + cantidad_en_carrito) > stock_disponible:
                print(f"Solo quedan {stock_disponible} unidades")
                continue
                
            if codigo in carrito:
                carrito[codigo] += cantidad
            else:
                carrito[codigo] = cantidad
                
            print("Agregado al carrito")
            
        except ValueError:
            print("Pon un numero valido")
            
    if not carrito:
        print("Venta cancelada, no hay nada en el carrito")
        return None
        
    subtotal = 0.0
    for cod, cant in carrito.items():
        subtotal += (inventario[cod]["precio"] * cant)
        
    descuento = 0.0
    if subtotal >= 100000:
        descuento = subtotal * 0.10
    elif subtotal >= 50000:
        descuento = subtotal * 0.05
        
    total_a_pagar = subtotal - descuento
    
    print("\n--- RESUMEN ---")
    print(f"Subtotal:  ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"TOTAL:     ${total_a_pagar}")
    
    while True:
        try:
            pago = float(input("\nCon cuanto paga?: $"))
            if pago < total_a_pagar:
                print(f"Falta plata, son ${total_a_pagar}")
            else:
                cambio = pago - total_a_pagar
                print(f"Cambio: ${cambio}")
                break
        except ValueError:
            print("Pon un numero")
            
    for cod, cant in carrito.items():
        inventario[cod]["stock"] -= cant
        
    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    
    venta_final = {
        "fecha": fecha_hoy,
        "total": total_a_pagar,
        "productos": carrito
    }
    
    print("Venta guardada")
    return venta_final