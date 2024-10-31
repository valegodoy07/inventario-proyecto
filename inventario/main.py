import sistema_inventario

print("Bienvenido bro :)")
while True:
    print("\nSelecciona una opcion: (1 - 4):\n1- Ver inventario\n2- Agregar producto\n3- Eliminar producto\n4- Salir")
    try:
        opcion = int(input("Opcion: "))

        if opcion == 1:
            sistema_inventario.mostrar_inventario()
        elif opcion == 2:
            sistema_inventario.agregar_producto()
        elif opcion == 3:
            sistema_inventario.eliminar_producto()
        elif opcion == 4:
            break
        else:
            print("Selecciona una opcion valida entre 1 y 4.")
    except ValueError:
        print("Error: Introduzca numeros unicamente")