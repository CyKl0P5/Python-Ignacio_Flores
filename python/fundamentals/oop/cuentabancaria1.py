#main class 
class BankAcc:
    def _init_(self, name , tasa_interes, balance):
        self.name = name
        self.balance = balance

    def deposit1(self, amount):
        self.balance += amount

    def make_withdraw(self, amount):
        self.balance -= amount

    def transfer(self, destinatario, cantidad):
        if cantidad > self.balance:
            print("No tiene el saldo suficiente para realizar esta transacción")
            






#user class
def deposito(self, amount):

def mostrar_info_cuenta(self):

def generar_interes(self):