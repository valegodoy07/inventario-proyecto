import sqlite3



conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS inventario(
               producto TEXT PRIMARY KEY,
               cantidad INTEGER
               )""")

class sistema_inventario():
    def agregar_producto():
        try:
            nombreP = input("Ingresa nombre del producto: ")
            cantidadP = int(input("Ingresa la cantidad: "))

            cursor.execute("INSERT INTO inventario (producto, cantidad) VALUES (?, ?)", (nombreP, cantidadP))
            conn.commit()
            print("Producto agregado exitosamente.")
        except ValueError:
            print("Por favor, ingresa un número válido para la cantidad.")
        except sqlite3.Error as e:
            print(f"Error al agregar producto: {e}")
    def eliminar_producto():
        

conn.close()
