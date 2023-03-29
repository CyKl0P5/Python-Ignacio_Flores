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
        self.make_withdraw(cantidad)
        destinatario.deposit1(cantidad)

    def accinfo(self):
        print(f"Usuario: {self.name}, Balance: {self.balance}")
        return self

    def money_trans(self, other_user, amount):
        self.make_withdraw(amount)
        other_user.balance += amount
        return self 

    def money_deposit(self, other_user, amount):
        self.deposit1(amount)
        other_user.balance += amount
        return self

    def percent(self):
        percent = self.balance * self.percent_tace
        self.balance += percent
        print(f"Interes generado: {percent}")
        return self





