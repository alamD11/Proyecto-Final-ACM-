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