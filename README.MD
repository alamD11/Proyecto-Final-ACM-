# TiendaPy - Sistema de Gestión para Don Aurelio

## 1. La Problemática
El proyecto nace de la necesidad de "Don Aurelio", el dueño de una tienda de barrio que maneja un inventario bastante grande (150 productos) y necesitaba una forma de automatizar sus procesos diarios. El problema principal era que llevar el control a mano provocaba desórdenes en el inventario, ventas sin registrar adecuadamente y falta de claridad sobre qué productos estaban a punto de agotarse o cuáles eran los más vendidos del día.

## 2. La Solución
Para solucionar esto, desarrollamos un sistema en Python que funciona por consola. La idea fue hacer un programa muy intuitivo y fácil de usar, donde Don Aurelio solo tenga que digitar números para moverse por el menú. 

El sistema cubre todo su ciclo de trabajo: permite buscar productos, registrar mercancía nueva, modificar precios, simular una venta (como un carrito de compras que calcula descuentos y vueltas), y al final del día generar un reporte de cierre de caja. Además, para que no pierda su información al cerrar el programa, todo se guarda de forma persistente en archivos de texto (`.txt`).

## 3. Organización del Código
Para no tener un solo archivo gigante y desordenado, aplicamos programación modular dividiendo el código según su responsabilidad. El proyecto quedó estructurado así:

* **`main.py`**: Es el archivo principal. Contiene el menú interactivo y conecta todas las demás funciones.
* **`inventario.py`**: Maneja toda la lógica de los productos (registro, búsqueda por categoría, modificación y el sistema de alertas de stock crítico).
* **`ventas.py`**: Se encarga del carrito de compras. Va sumando productos, aplica descuentos automáticos si la compra supera los 50k o 100k, y calcula el cambio a entregar.
* **`reportes.py`**: Lee el registro de ventas y calcula el total del día, el producto más vendido, el ticket promedio y las categorías que se movieron.
* **`persistencia.py`**: Es el puente entre el programa y los archivos `.txt`. Se encarga de cargar el inventario al iniciar y guardar los cambios y las ventas utilizando el formato separado por pipes (`|`).
* **Carpeta `data/`**: Contiene la base de datos simulada (`inventario.txt` con los 150 productos y `ventas.txt`).

## 4. Prevención de Errores y Validaciones
Para asegurar que el programa no se cierre de golpe (no se "estalle") si el usuario se equivoca digitando algo, implementamos varias comprobaciones usando condicionales y bloques `try/except`:

* **Validación de tipos de datos:** Al pedir precios, cantidades o el pago del cliente, el programa verifica que se ingresen números válidos. Si se ingresa una letra por error, muestra un mensaje amigable y vuelve a preguntar en lugar de mostrar un error de consola.
* **Control de Stock:** En el módulo de ventas, el sistema comprueba que la cantidad solicitada no supere el stock real disponible. También descuenta el stock automáticamente tras cada venta.
* **Control de negativos:** No se permite registrar productos con precios o inventarios menores a cero.
* **Manejo de archivos vacíos:** Si el programa se inicia por primera vez o no hay ventas registradas en el día, el sistema lo detecta y muestra un aviso en lugar de intentar leer datos que no existen.
* **Menú a prueba de fallos:** Si en el menú principal se digita una opción fuera del rango (1-7) o una letra, simplemente avisa que es inválido y vuelve a cargar las opciones.