
class SistemaInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad

    def eliminar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            if cantidad >= self.inventario[nombre]:
                del self.inventario[nombre]
            else:
                self.inventario[nombre] -= cantidad
        else:
            print("El producto no está en el inventario.")

    def actualizar_inventario(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] = cantidad
        else:
            print("El producto no está en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for nombre, cantidad in self.inventario.items():
            print(f"{nombre}: {cantidad}")
