class Inventario:
    def __init__(self):
        self.productos = {}

#todos los elementos en python son objetos
#un objeto posee atributos y metodos

    def agregar_producto(self,nombre,precio,stock):
        nombre = nombre.strip().lower()
        if nombre in self.productos:
            raise ValueError("El producto ya existe")
        
        self.productos[nombre] = {"precio": precio, "stock": stock}

    #estructura del diccionario
    # productos = {
    #     'manzanas': {"precio": 600, "stock":4},
    #     'peras':{"precio":1200, "stock":5}
    # }

    def ver_productos(self):
        return self.productos
    
    def consultar_producto(self,nombre):
        return self.productos.get(nombre, "Producto no encontrado")
    
    def eliminar_producto(self,nombre):
        if nombre not in self.productos:
            raise ValueError("El producto no existe")
        
        del self.productos[nombre]

    def actualizar_precio(self, nombre, precio):
        if nombre not in self.productos:
            raise ValueError("El producto no existe")
        
        self.productos[nombre]["precio"] = precio
        return self.productos[nombre]["precio"]
    
    def agregar_stock(self,nombre, stock):
        if nombre not in self.productos:
            raise ValueError("El producto no existe")
        
        self.productos[nombre]["stock"] += stock
        return self.productos[nombre]["stock"]