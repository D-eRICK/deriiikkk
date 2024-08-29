class Tienda:
    def __init__(self):
        self.inventario = {}  # Lista para almacenar los productos y sus cantidades
        self.ventas = []  # Lista para almacenar las ventas realizadas

    def agregar_producto(self, nombre, cantidad, precio_venta):
        if nombre in self.inventario:
            self.inventario[nombre]['cantidad'] += cantidad
        else:
            self.inventario[nombre] = {'cantidad': cantidad, 'precio': precio_venta}
        print(f"Producto '{nombre}' agregado con éxito. Cantidad: {cantidad}, Precio de venta: ${precio_venta:.2f}")

    def vender_producto(self, nombre, cantidad, dinero_recibido):
        if nombre not in self.inventario:
            print(f"El producto '{nombre}' no está en inventario.")
            return

        if self.inventario[nombre]['cantidad'] < cantidad:
            print(f"No hay suficiente cantidad de '{nombre}' en inventario.")
            return

        precio_total = self.inventario[nombre]['precio'] * cantidad
        if dinero_recibido < precio_total:
            print(f"Dinero recibido insuficiente. Total a pagar: ${precio_total:.2f}")
            return

        self.inventario[nombre]['cantidad'] -= cantidad
        self.ventas.append((nombre, cantidad, precio_total))
        cambio = dinero_recibido - precio_total
        print(f"Venta realizada con éxito. Total: ${precio_total:.2f}. Cambio: ${cambio:.2f}")

    def mostrar_inventario(self):
        print("\nInventario actual:")
        for producto, detalles in self.inventario.items():
            print(f"{producto}: {detalles['cantidad']} unidades, Precio: ${detalles['precio']:.2f}")
        print()

    def mostrar_ventas(self):
        print("\nVentas realizadas:")
        for venta in self.ventas:
            print(f"Producto: {venta[0]}, Cantidad: {venta[1]}, Total: ${venta[2]:.2f}")
        print()

# Ejemplo
tienda = Tienda()

# Para agregar productos
tienda.agregar_producto("Jabón", 100, 1.50)
tienda.agregar_producto("Shampoo", 50, 3.25)

# Mostrar el inventario
tienda.mostrar_inventario()

# Realizar ventas
tienda.vender_producto("Jabón", 2, 5.00)
tienda.vender_producto("Shampoo", 1, 5.00)

#ventas realizadas
tienda.mostrar_ventas()

# Mostrar inventario actualizado
tienda.mostrar_inventario()
