local_val = "unicornios magicos"
def square(x):
    return x * x

class Usuario:
    def __init__(self, name):
        self.name = name
    
    def di_hola(self):
        return "Hola"
    
print(square(5))
user = Usuario("Franco")
print(user.name)
print(user.di_hola())
print(__name__)

if __name__ == "__main__":
    print("El archivo se esta ejecutando directamente")
else:
    print("El archivo se esta ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)