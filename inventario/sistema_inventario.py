import sqlite3
import pandas as pd

conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventario (
        producto TEXT PRIMARY KEY,
        stock INTEGER
    )
''')
conn.commit()

def mostrar_inventario():
    cursor.execute("SELECT * FROM inventario")
    results = cursor.fetchall()
    results_df = pd.DataFrame(results, columns=["Producto", "Stock"])
    print("\nInventario:\n", results_df)

def agregar_producto():
    print("Escribe el producto a agregar:")
    producto = input(" ")
    print("Ahora escribe el stock del producto:")
    stock = int(input(" "))

    cursor.execute("SELECT * FROM inventario WHERE producto = ?", (producto,))
    producto_existente = cursor.fetchone()

    if producto_existente:
        print(f"El producto '{producto}' ya existe en el inventario con una cantidad de {producto_existente[1]}.")
    else:
        cursor.execute("INSERT INTO inventario (producto, stock) VALUES (?, ?)", (producto, stock))
        conn.commit()
        print(f"Producto '{producto}' agregado con stock {stock}.")

def eliminar_producto():
    print("Escribe el producto que deseas eliminar:")
    producto = input(" ")

    cursor.execute("DELETE FROM inventario WHERE producto = ?", (producto,))
    conn.commit()
    print(f"Producto '{producto}' eliminado del inventario.")