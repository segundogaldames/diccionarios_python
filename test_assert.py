from inventario import Inventario

inv = Inventario()

inv.agregar_producto("laptop",350000,10)

assert "laptop" in inv.ver_productos()
assert inv.consultar_producto("laptop")["precio"] == 350000
assert inv.consultar_producto("laptop")["stock"] == 10

inv.actualizar_precio("laptop",380000)
assert inv.consultar_producto("laptop")["precio"] == 380000

inv.agregar_stock("laptop",5)
assert inv.consultar_producto("laptop")["stock"] == 15

inv.eliminar_producto("laptop")
assert inv.consultar_producto("laptop") == "Producto no encontrado"

print("Las pruebas pasaron correctamente")