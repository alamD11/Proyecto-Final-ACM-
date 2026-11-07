import os

RUTA_INVENTARIO = "data/inventario.txt"
RUTA_VENTAS = "data/ventas.txt"

def cargar_inventario():
    """Carga los productos desde inventario.txt a un diccionario."""
    inventario = {}
    if not os.path.exists(RUTA_INVENTARIO):
        return inventario
        
    with open(RUTA_INVENTARIO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                # Sigue el formato , codigo|nombre|categoria|precio|stock|stock_minimo|proveedor
                datos = linea.split("|")
                if len(datos) == 7:
                    codigo = datos[0]
                    inventario[codigo] = {
                        "nombre": datos[1],
                        "categoria": datos[2],
                        "precio": float(datos[3]),
                        "stock": int(datos[4]),
                        "stock_minimo": int(datos[5]),
                        "proveedor": datos[6]
                    }
    return inventario

def guardar_inventario(inventario):
    """Guarda el diccionario de productos en inventario.txt sobrescribiendo el archivo."""
    os.makedirs("data", exist_ok=True)
    with open(RUTA_INVENTARIO, "w", encoding="utf-8") as archivo:
        for codigo, prod in inventario.items():
            linea = f"{codigo}|{prod['nombre']}|{prod['categoria']}|{prod['precio']}|{prod['stock']}|{prod['stock_minimo']}|{prod['proveedor']}\n"
            archivo.write(linea)
def guardar_venta(venta):
    """Guarda una venta en el archivo ventas.txt."""
    os.makedirs("data", exist_ok=True)
    
    # Armamos la cadena de productos del carrito (ejem: LAC001:2;BEB003:1)
    lista_productos = []
    for codigo, cantidad in venta["productos"].items():
        lista_productos.append(f"{codigo}:{cantidad}")
    
    productos_texto = ";".join(lista_productos)
    
    # Escribimos la linea completa
    linea = f"{venta['fecha']}|{venta['total']}|{productos_texto}\n"
    
    # Usamos "a"(append) para no borrar las ventas anteriores
    with open(RUTA_VENTAS, "a", encoding="utf-8") as archivo:
        archivo.write(linea)