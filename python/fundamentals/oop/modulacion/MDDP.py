class Ninja:
    def __init__(self, nombre, apellido, premios, comida_mascotas, nombre_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascotas = comida_mascotas
        self.nombre_mascotas = nombre_mascota

    def caminar(self):
        print("Sale a pasear")

    def alimentar(self):
        print("Se a alimentado a la mascota")

    def bañar(self):
        print("Se a bañado a la mascota")

usr = Ninja("Franco", "Carrasco", 3, 2, "Luna")