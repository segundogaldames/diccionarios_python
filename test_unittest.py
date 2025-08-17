import unittest
from inventario import Inventario

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inv = Inventario()
        self.inv.agregar_producto("mouse",15000,20)

    def test_agregar_producto(self):
        self.inv.agregar_producto("teclado",18000,10)
        self.assertIn("teclado",self.inv.ver_productos())

    def test_consultar_producto(self):
        producto = self.inv.consultar_producto("mouse")
        self.assertEqual(producto["precio"],15000)
        self.assertEqual(producto["stock"],20)

    def test_actualizar_precio(self):
        nuevo_precio = self.inv.actualizar_precio("mouse",18000)
        self.assertEqual(nuevo_precio,18000)

    def test_agregar_stock(self):
        nuevo_stock = self.inv.agregar_stock("mouse",10)
        self.assertEqual(nuevo_stock,30)

    def eliminar_producto(self):
        self.inv.eliminar_producto("mouse")
        self.assertEqual(self.inv.consultar_producto("mouse"),"Producto no encontrado")

if __name__ == "__main__":
    unittest.main()