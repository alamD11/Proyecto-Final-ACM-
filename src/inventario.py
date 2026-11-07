def registrar_producto(inventario, codigo, nombre, categoria, precio, stock, stock_minimo, proveedor):
    if codigo in inventario:
        print(f"Error: el codigo '{codigo}' ya existe")
        return False
    
    if precio <= 0 or stock < 0 or stock_minimo < 0:
        print("Error: no pongas numeros negativos")
        return False

    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }
    print(f"Producto '{nombre}' guardado bien")
    return True

def consultar_producto(inventario, codigo):
    if codigo in inventario:
        return inventario[codigo]
    print(f"No se encontro el codigo '{codigo}'")
    return None

def eliminar_producto(inventario, codigo):
    if codigo in inventario:
        del inventario[codigo]
        print(f"Producto '{codigo}' eliminado")
        return True
    print(f"El producto '{codigo}' no existe")
    return False

def obtener_alertas_stock(inventario):
    alertas = {}
    for codigo, prod in inventario.items():
        if prod["stock"] <= prod["stock_minimo"]:
            proveedor = prod["proveedor"]
            if proveedor not in alertas:
                alertas[proveedor] = []
            
            producto_alerta = prod.copy()
            producto_alerta["codigo"] = codigo
            
            if prod["stock"] == 0:
                producto_alerta["estado"] = "AGOTADO"
            else:
                producto_alerta["estado"] = "Critico"
                
            alertas[proveedor].append(producto_alerta)
    return alertas

def buscar_por_categoria(inventario, categoria):
    encontrados = {}
    for codigo, prod in inventario.items():
        if prod["categoria"].lower() == categoria.lower():
            encontrados[codigo] = prod
    return encontrados

def modificar_producto(inventario, codigo):
    if codigo not in inventario:
        print(f"Error: el producto '{codigo}' no existe")
        return False
        
    print(f"Modificando: {inventario[codigo]['nombre']}")
    try:
        nuevo_precio = float(input("Nuevo precio: "))
        nuevo_stock = int(input("Nuevo stock: "))
        
        if nuevo_precio <= 0 or nuevo_stock < 0:
            print("Error: numeros validos porfa")
            return False
            
        inventario[codigo]["precio"] = nuevo_precio
        inventario[codigo]["stock"] = nuevo_stock
        print("Producto actualizado")
        return True
    except ValueError:
        print("Error: pon numeros")
        return False