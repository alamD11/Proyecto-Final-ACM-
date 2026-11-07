from persistencia import cargar_inventario, guardar_inventario, guardar_venta
from inventario import registrar_producto, obtener_alertas_stock, modificar_producto, buscar_por_categoria
from ventas import procesar_venta
from reportes import generar_cierre_dia
from tabulate import tabulate

def mostrar_menu():
    print("\n" + "="*40)
    print("         TIENDAPY - DON AURELIO")
    print("="*40)
    print("1. Ver inventario o buscar por categoria")
    print("2. Registrar un nuevo producto")
    print("3. Modificar precio o stock")
    print("4. Ver alertas de stock")
    print("5. Registrar una venta")
    print("6. Generar cierre del dia")
    print("7. Guardar y salir")
    print("="*40)
    return input("Elige una opcion (1-7): ")

def main():
    inventario = cargar_inventario()
    print(f"\nCargados {len(inventario)} productos")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            if not inventario:
                print("\nEl inventario esta vacio")
            else:
                print("\nOpciones:")
                print("1. Ver todo el inventario")
                print("2. Buscar por categoria")
                sub_op = input("Elige una opcion (1 o 2): ").strip()
                
                productos_a_mostrar = inventario
                
                if sub_op == "2":
                    cat = input("Ingresa la categoria (ej. Lacteos, Aseo): ").strip()
                    productos_a_mostrar = buscar_por_categoria(inventario, cat)
                    if not productos_a_mostrar:
                        print(f"No hay productos en la categoria '{cat}'")
                        continue
                elif sub_op != "1":
                    print("Opcion invalida, volviendo al menu...")
                    continue
                
                tabla = []
                for cod, prod in productos_a_mostrar.items():
                    tabla.append([cod, prod['nombre'], prod['categoria'], f"${prod['precio']}", prod['stock'], prod['proveedor']])
                headers = ["Codigo", "Nombre", "Categoria", "Precio", "Stock", "Proveedor"]
                print("\n" + tabulate(tabla, headers=headers, tablefmt="grid"))

        elif opcion == "2":
            print("\n--- Registrar producto ---")
            codigo = input("Codigo (ej. LAC005): ").strip().upper()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoria: ").strip()
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock actual: "))
                stock_minimo = int(input("Stock minimo: "))
            except ValueError:
                print("\nError: el precio y stock deben ser numeros")
                continue
            proveedor = input("Proveedor: ").strip()
            registrar_producto(inventario, codigo, nombre, categoria, precio, stock, stock_minimo, proveedor)

        elif opcion == "3":
            print("\n--- Modificar producto ---")
            codigo = input("Ingresa el codigo del producto: ").strip().upper()
            modificar_producto(inventario, codigo)

        elif opcion == "4":
            alertas = obtener_alertas_stock(inventario)
            if not alertas:
                print("\nNo hay alertas de stock, todo bien")
            else:
                print("\n--- ALERTAS POR PROVEEDOR ---")
                for prov, prods in alertas.items():
                    print(f"\nProveedor: {prov}")
                    tabla_alertas = [[p['codigo'], p['nombre'], p['stock'], p['estado']] for p in prods]
                    print(tabulate(tabla_alertas, headers=["Codigo", "Producto", "Stock", "Estado"], tablefmt="simple"))

        elif opcion == "5":
            venta_realizada = procesar_venta(inventario)
            if venta_realizada:
                guardar_venta(venta_realizada)
                guardar_inventario(inventario)

        elif opcion == "6":
            generar_cierre_dia(inventario)

        elif opcion == "7":
            guardar_inventario(inventario)
            print("\nDatos guardados. Chao!")
            break
        else:
            print("\nOpcion invalida, elige del 1 al 7")

if __name__ == "__main__":
    main()