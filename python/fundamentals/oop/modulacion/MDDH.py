import MDDP
from MDDP import Ninja

class mascota(Ninja):
    def __init__(self, nombre_mascota, tipo, golosinas):
        self.nombre_mascota = nombre_mascota
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 0
        self.energia = 100

    def dormir(self):
        self.energia += 25
        print(self.energia)
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        print(self.salud, self.energia)
        super().alimentar()
        return self
    
    def jugar(self):
        self.salud += 5
        print(self.salud)
        super().caminar()
        return self
    
    def ruido(self):
        if self.tipo == "Gato":
            print("Meow")
        elif self.tipo == "Perro":
            print("Guau")
        super().bañar()
        return self

mascota1 = mascota(MDDP.usr.nombre_mascotas, "Gato", 10)

mascota1.dormir().comer().jugar().ruido()