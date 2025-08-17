from inventario import Inventario
from menu import Menu

inventario = Inventario()
menu = Menu()

def validar_cero(valor):
    while valor <= 0:
        valor = int(input("El valor ingresado no puede ser menor o igual a cero: "))

    return valor

estado = True
while estado:
    try:
        menu.menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1: #agregar producto
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            while estado: 
                try: #validamos el ingreso de precio
                    precio = int(input("Ingrese el precio: "))
                    precio = validar_cero(precio)
                    break
                except ValueError:
                    print("Ingrese un número entero para el precio")

            while estado:
                try: #validamos el ingreso de stock
                    stock = int(input("Ingrese el stock del producto: "))
                    stock = validar_cero(stock)
                    break
                except ValueError:
                    print("Ingrese un número entero para el stock")

            inventario.agregar_producto(nombre,precio,stock)
            print("Producto agregado")

        elif opcion == 2: #Ver productos
            productos = inventario.ver_productos()
            if not productos:
                print("No hay productos registrados")
            else:
                for nombre, datos in productos.items():
                    print(f"- {nombre}: ${datos["precio"]} | stock: {datos["stock"]}")

        elif opcion == 3: #consultar producto
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            producto = inventario.consultar_producto(nombre)
            print(producto if producto else "Producto no encontrado")
        elif opcion == 4: #eliminar producto
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            try:
                inventario.eliminar_producto(nombre)
                print("Producto eliminado correctamente")
            except ValueError:
                print("El producto no se ha eliminado")

        elif opcion == 5: #actualizar precio
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
        
            try:
                precio = int(input("Ingrese el precio del producto: "))
                precio = validar_cero(precio)
            except ValueError:
                print("Ingrese un número entero")

            nuevo_precio = inventario.actualizar_precio(nombre, precio)
            print(f"Nuevo precio de {nombre}: ${nuevo_precio}")

        elif opcion == 6: #agregar stock
            nombre = input("Ingrese el nombre del producto: ").strip().lower()
            while estado:
                try:
                    stock = int(input("Ingrese el nuevo stock del producto: "))
                    stock = validar_cero(stock)
                    break
                except ValueError:
                    print("Ingrese un número entero para el nuevo stock")

            nuevo_stock = inventario.agregar_stock(nombre,stock)
            print(f"El nuevo stock de {nombre} es {nuevo_stock}")
            
        elif opcion == 7: #opcion salir
            print("Muchas gracias por usar nuestra aplicación")
            estado = False

    except ValueError:
        print("Error: dato incorrecto")