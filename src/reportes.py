import os
import datetime
from persistencia import RUTA_VENTAS

def generar_cierre_dia(inventario):
    if not os.path.exists(RUTA_VENTAS):
        print("No hay ventas para hacer cierre hoy")
        return

    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    
    total_vendido = 0.0
    num_transacciones = 0
    cantidades_vendidas = {} 
    categorias_movimiento = [] 
    
    with open(RUTA_VENTAS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
                
            partes = linea.split("|")
            if len(partes) != 3:
                continue
                
            fecha_venta = partes[0]
            
            if fecha_venta == fecha_hoy:
                total_venta = float(partes[1])
                productos_str = partes[2]
                
                total_vendido += total_venta
                num_transacciones += 1
                
                items = productos_str.split(";")
                for item in items:
                    if ":" in item:
                        codigo, cantidad_str = item.split(":")
                        cantidad = int(cantidad_str)
                        
                        if codigo in cantidades_vendidas:
                            cantidades_vendidas[codigo] += cantidad
                        else:
                            cantidades_vendidas[codigo] = cantidad
                            
                        if codigo in inventario:
                            categoria = inventario[codigo]["categoria"]
                            if categoria not in categorias_movimiento:
                                categorias_movimiento.append(categoria)

    print("\n" + "="*40)
    print(f"        CIERRE DE CAJA {fecha_hoy}")
    print("="*40)
    
    if num_transacciones == 0:
        print("Hoy no se vendio nada")
        return
        
    print(f"Total vendido:    ${total_vendido}")
    print(f"Transacciones:    {num_transacciones}")
    
    ticket_promedio = total_vendido / num_transacciones
    print(f"Ticket promedio:  ${ticket_promedio:.2f}")
    
    if cantidades_vendidas:
        max_cantidad = 0
        codigo_mas_vendido = ""
        for cod, cant in cantidades_vendidas.items():
            if cant > max_cantidad:
                max_cantidad = cant
                codigo_mas_vendido = cod
        
        nombre_mas_vendido = inventario[codigo_mas_vendido]["nombre"] if codigo_mas_vendido in inventario else codigo_mas_vendido
        print(f"Mas vendido:      {nombre_mas_vendido} ({max_cantidad} unds)")
        
    texto_categorias = ", ".join(categorias_movimiento)
    print(f"Categorias q se movieron: {texto_categorias}")
    
    productos_sin_ventas = []
    for codigo, prod in inventario.items():
        if codigo not in cantidades_vendidas:
            productos_sin_ventas.append(prod["nombre"])
            
    print(f"\nProductos que no se vendieron ({len(productos_sin_ventas)}):")
    for nombre in productos_sin_ventas[:5]:
        print(f"- {nombre}")
    if len(productos_sin_ventas) > 5:
        print(f"... y {len(productos_sin_ventas) - 5} mas")
    
    print("="*40)