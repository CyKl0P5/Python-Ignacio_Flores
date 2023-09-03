class Producto:
    def __init__(self, name, precio, cantidad, id):
        self.name = name
        self.precio = precio
        self.cantidad = cantidad
        self.id = id

    def print_info(self):
        print(f"Nombre: {self.name}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"ID: {self.id}")
        print("--------------------------------------------------")

    def actualizar_precio(self, amount):
        self.precio = int(amount)

    def realizar_descuento(self, descuento):
        descuento = self.precio * descuento
        self.precio -= descuento
        return self