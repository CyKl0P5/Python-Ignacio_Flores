from Producto import Producto

class Tienda:
    def __init__(self, name, direccion):
        self.name = name
        self.direccion = direccion
        self.ganancia = 0
        self.productos = []
        self.productosN = []

    def agregar_productos(self, producto):
        self.productos.append(producto)
        self.productosN.append(producto.name)
        return self

    def vender_productos(self, producto):
        self.productos.remove(producto)
        self.ganancia += producto.precio
        return self
    
    def inflacion(self, inflacion):
        for producto in self.productos:
            producto.actualizar_precio(producto.precio * (1 + inflacion))

    def liquidacion(self, descuento):
        total = 0
        for producto in self.productos:
            precio_descuento = producto.precio * (1 - descuento)
            total += precio_descuento
        self.ganancia += total
        self.productos = []
        return self

    def info_tienda(self):
        print(f"Nombre: {self.name}")
        print(f"Direccion: {self.direccion}")
        print(f"Dinero: {self.ganancia}")
        print("Productos disponibles:")
        print(self.productosN)
        print("--------------------------------------------------")
        return self