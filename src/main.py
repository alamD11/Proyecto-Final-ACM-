from persistencia import cargar_inventario, guardar_inventario
from inventario import registrar_producto, obtener_alertas_stock
from tabulate import tabulate

def mostrar_menu():
    """Imprime las opciones del sistema."""
    print("\n" + "="*35)
    print("        TIENDA - DON AURELIO")
    print("="*35)
    print("1. Ver Inventario completo")
    print("2. Registrar un nuevo producto")
    print("3. Ver alertas de stock crítico")
    print("4. Guardar y Salir")
    print("="*35)
    return input("Seleccione una opción (1-4): ")

def main():
    # Cargar el inventario al iniciar
    inventario = cargar_inventario()
    print(f"\n[SISTEMA] Se cargaron {len(inventario)} productos desde la base de datos.")

    # Ciclo activo hasta que el usuario decida salir
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            if not inventario:
                print("\nEl inventario está vacío.")
            else:
                tabla = []
                for cod, prod in inventario.items():
                    tabla.append([cod, prod['nombre'], prod['categoria'], f"${prod['precio']}", prod['stock'], prod['proveedor']])
                headers = ["Código", "Nombre", "Categoría", "Precio", "Stock", "Proveedor"]
                print("\n" + tabulate(tabla, headers=headers, tablefmt="grid"))

        elif opcion == "2":
            print("\n--- Registro de Producto ---")
            codigo = input("Código único (ej. LAC005): ").strip().upper()
            nombre = input("Nombre comercial: ").strip()
            categoria = input("Categoría: ").strip()
            
            # Validación básica de errores de digitación
            try:
                precio = float(input("Precio de venta: "))
                stock = int(input("Stock disponible: "))
                stock_minimo = int(input("Stock mínimo de alerta: "))
            except ValueError:
                print("\n[ERROR] El precio y los stocks deben ser valores numéricos. Intente de nuevo.")
                continue
                
            proveedor = input("Proveedor habitual: ").strip()
            
            registrar_producto(inventario, codigo, nombre, categoria, precio, stock, stock_minimo, proveedor)

        elif opcion == "3":
            alertas = obtener_alertas_stock(inventario)
            if not alertas:
                print("\n[INFO] No hay productos en estado crítico o agotados.")
            else:
                print("\n--- ALERTAS AGRUPADAS POR PROVEEDOR ---")
                for prov, prods in alertas.items():
                    print(f"\nProveedor: {prov}")
                    tabla_alertas = [[p['codigo'], p['nombre'], p['stock'], p['estado']] for p in prods]
                    print(tabulate(tabla_alertas, headers=["Código", "Producto", "Stock Actual", "Estado"], tablefmt="simple"))

        elif opcion == "4":
            # Guardar al salir
            guardar_inventario(inventario)
            print("\n[SISTEMA] Datos guardados exitosamente. ¡Hasta luego!")
            break
        else:
            print("\n[ERROR] Opción inválida. Digite un número del 1 al 4.")

if __name__ == "__main__":
    main()
