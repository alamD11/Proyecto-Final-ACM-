import datetime

def procesar_venta(inventario):
    """Maneja el proceso de venta en consola."""
    carrito = {}
    print("\n--- NUEVO REGISTRO DE VENTA ---")
    
    while True:
        codigo = input("Ingrese el codigo del producto (o '0' para cobrar): ").strip().upper()
        
        if codigo == '0':
            break
            
        if codigo not in inventario:
            print("Producto no encontrado.")
            continue
            
        try:
            cantidad = int(input(f"¿Cuantas unidades de {inventario[codigo]['nombre']}?: "))
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue
                
            # Validar que no se venda mas de lo que hay en stock
            stock_disponible = inventario[codigo]["stock"]
            
            # Si ya está en el carrito, sumar la cantidad para validar el stock total
            cantidad_en_carrito = carrito.get(codigo, 0)
            
            if (cantidad + cantidad_en_carrito) > stock_disponible:
                print(f"Error: Solo hay {stock_disponible} unidades disponibles en total.")
                continue
                
            # Agregar al carrito
            if codigo in carrito:
                carrito[codigo] += cantidad
            else:
                carrito[codigo] = cantidad
                
            print("Producto agregado al carrito.")
            
        except ValueError:
            print("Error: Por favor ingrese un número entero.")
            
    # Si no compra nada... salir
    if not carrito:
        print("Venta cancelada (carrito vacío).")
        return None
        
    # Calcular subtotales
    subtotal = 0.0
    for cod, cant in carrito.items():
        subtotal += (inventario[cod]["precio"] * cant)
        
    # Aplicar reglas de descuento
    descuento = 0.0
    if subtotal >= 100000:
        descuento = subtotal * 0.10
    elif subtotal >= 50000:
        descuento = subtotal * 0.05
        
    total_a_pagar = subtotal - descuento
    
    print("\n--- RESUMEN DE COMPRA ---")
    print(f"Subtotal:  ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"TOTAL:     ${total_a_pagar}")
    
    # Proceso de pago
    while True:
        try:
            pago = float(input("\nEfectivo recibido: $"))
            if pago < total_a_pagar:
                print(f"Falta dinero. El total es ${total_a_pagar}")
            else:
                cambio = pago - total_a_pagar
                print(f"Cambio a entregar: ${cambio}")
                break
        except ValueError:
            print("Ingrese una cantidad de dinero válida.")
            
    # Descontar el stock del inventario
    for cod, cant in carrito.items():
        inventario[cod]["stock"] -= cant
        
    # Retornar los datos para guardarlos en persistencia
    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    
    venta_final = {
        "fecha": fecha_hoy,
        "total": total_a_pagar,
        "productos": carrito
    }
    
    print("---Hiciste la compra we---")
    return venta_final