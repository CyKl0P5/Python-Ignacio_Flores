from Tienda import Tienda
from Producto import Producto
import random

testT = Tienda("Tu Mamita Store", "Av. Tu mamá")
test = Producto("Queso", 700, 10, random.randint(0, 100))
testTO = Producto("Tomate", 1000, 10, random.randint(0, 100))

testT.agregar_productos(testTO).agregar_productos(test)

testT.info_tienda()
test.print_info()
testTO.print_info()
test.actualizar_precio(750)
testTO.realizar_descuento(0.2)
test.print_info()
testTO.print_info()
testT.inflacion(0.12)
test.print_info()
testTO.print_info()
testT.liquidacion(0.20)
testT.info_tienda()