class ventas_sofi08:  # Primero que todo creamos la clase
    print('*** Bienvenido al Sistema de gestión de inventario de Sofi08 Soft ***')

    def __init__(pila_ventas):
        # Inicializamos la Pila con la lista vacía y creamos listas de productos, precios, y cantidades.
        pila_ventas.pila_ventas = []
        pila_ventas.productos = ['Casco', 'Botas', 'Chaqueta', 'Guantes', 'Rodilleras', 'Coderas', 'Pinlock']
        pila_ventas.precios = [120000, 120000, 110000, 35000, 39990, 29990, 19990]
        pila_ventas.cantidades = [75, 50, 67, 120, 65, 80, 200]

    def push(pila_ventas, producto, cantidad):  # Operación para agregar una venta a la pila
        if producto in pila_ventas.productos:
            index = pila_ventas.productos.index(producto)
            if pila_ventas.cantidades[index] >= cantidad:
                pila_ventas.cantidades[index] -= cantidad
                precio_total = pila_ventas.precios[index] * cantidad
                venta = {'producto': producto, 'cantidad': cantidad, 'precio': precio_total}
                pila_ventas.pila_ventas.append(venta)
                print(f'Venta agregada: {producto} - Cantidad: {cantidad} - Precio total: ${precio_total}')
            else:
                print(f'No hay suficiente stock de {producto}. Stock disponible: {pila_ventas.cantidades[index]}')
        else:
            print("Producto no disponible en la tienda.")

    def pop(pila_ventas):  # Operación para eliminar la última venta de la pila
        if not pila_ventas.esta_vacia():
            venta_eliminada = pila_ventas.pila_ventas.pop()
            print(f'Venta eliminada: {venta_eliminada["producto"]} - Cantidad: {venta_eliminada["cantidad"]}')
            index = pila_ventas.productos.index(venta_eliminada['producto'])
            pila_ventas.cantidades[index] += venta_eliminada['cantidad']
            return venta_eliminada
        else:
            print('No hay ventas para eliminar.')
            return None

    def esta_vacia(pila_ventas):  # Verifica si la pila está vacía
        return len(pila_ventas.pila_ventas) == 0

    def mostrar_ventas(pila_ventas):  # Muestra todas las ventas en la pila
        if pila_ventas.esta_vacia():
            print('No hay ventas registradas.')
        else:
            print('Ventas del día:')
            for venta in reversed(pila_ventas.pila_ventas):  # Mostramos desde la última venta agregada
                print(f'Producto: {venta["producto"]} - Cantidad: {venta["cantidad"]} - Precio: ${venta["precio"]}')

    def mostrar_stock(pila_ventas):  # Muestra el stock actual
        print("Stock actual:")
        for i, producto in enumerate(pila_ventas.productos):
            print(f'{producto}: {pila_ventas.cantidades[i]} unidades disponibles - Precio: ${pila_ventas.precios[i]} CLP')

# Crear una instancia de la pila de ventas
pila_ventas = ventas_sofi08()

# Función para agregar una venta de producto
def agregar_venta(pila, producto, cantidad):
    pila.push(producto, cantidad)

# Mostrar el stock inicial
pila_ventas.mostrar_stock()

# Ejemplos de ventas en la tienda de ropa para motociclistas
agregar_venta(pila_ventas, 'Casco', 2)
agregar_venta(pila_ventas, 'Botas', 1)
agregar_venta(pila_ventas, 'Chaqueta', 1)
agregar_venta(pila_ventas, 'Guantes', 3)
agregar_venta(pila_ventas, 'Rodilleras', 1)
agregar_venta(pila_ventas, 'Coderas', 1)
agregar_venta(pila_ventas, 'Pinlock', 1)

# Mostrar las ventas realizadas durante el día
pila_ventas.mostrar_ventas()

# Mostrar el stock actualizado después de las ventas
pila_ventas.mostrar_stock()
