from sistema import SistemaInventario

def agregar_producto(sistema, nombre, cantidad):
    print(f"Elegido: Agregar producto '{nombre}' con cantidad {cantidad}.")
    sistema.agregar_producto(nombre, cantidad)

def eliminar_producto(sistema, nombre, cantidad):
    print(f"Elegido: Eliminar producto '{nombre}' con cantidad {cantidad}.")
    sistema.eliminar_producto(nombre, cantidad)

def actualizar_inventario(sistema, nombre, cantidad):
    print(f"Elegido: Actualizar producto '{nombre}' con cantidad {cantidad}.")
    sistema.actualizar_inventario(nombre, cantidad)

def mostrar_inventario(sistema):
    print("Elegido: Mostrar inventario.")
    sistema.mostrar_inventario()