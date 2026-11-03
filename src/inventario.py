def registrar_producto(inventario, codigo, nombre, categoria, precio, stock, stock_minimo, proveedor):
    """Registra un nuevo producto validando las reglas de negocio."""
    # Los códigos de producto no pueden repetirse
    if codigo in inventario:
        print(f"Error: El código de producto '{codigo}' ya existe.")
        return False
    
    # No se permiten precios ni cantidades negativas
    if precio <= 0 or stock < 0 or stock_minimo < 0:
        print("Error: No se permiten precios ni cantidades negativas.")
        return False

    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }
    print(f"Producto '{nombre}' registrado con éxito.")
    return True

def consultar_producto(inventario, codigo):
    """Retorna los datos de un producto si existe."""
    if codigo in inventario:
        return inventario[codigo]
    print(f"Error: No se encontró ningún producto con el código '{codigo}'.")
    return None

def eliminar_producto(inventario, codigo):
    """Elimina un producto del inventario."""
    if codigo in inventario:
        del inventario[codigo]
        print(f"Producto '{codigo}' eliminado del inventario.")
        return True
    print(f"Error: El producto '{codigo}' no existe.")
    return False

def obtener_alertas_stock(inventario):
    """Lista productos con stock crítico agrupados por proveedor."""
    alertas = {}
    for codigo, prod in inventario.items():
        # Validar si el stock es menor o igual al mínimo
        if prod["stock"] <= prod["stock_minimo"]:
            proveedor = prod["proveedor"]
            if proveedor not in alertas:
                alertas[proveedor] = []
            
            producto_alerta = prod.copy()
            producto_alerta["codigo"] = codigo
            
            # Un producto con stock cero debe aparecer como agotado
            if prod["stock"] == 0:
                producto_alerta["estado"] = "AGOTADO"
            else:
                producto_alerta["estado"] = "Stock Crítico"
                
            alertas[proveedor].append(producto_alerta)
    return alertas