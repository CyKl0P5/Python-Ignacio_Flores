#main class 
class BankAcc:
    def __init__(self, name, balance, percent_tace):
        self.name = name
        self.balance = balance
        self.percent_tace = percent_tace

    def deposit1(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def transfer(self, destinatario, cantidad):
        if cantidad > self.balance:
            print("No tiene el saldo suficiente para realizar esta transacción")
        self.make_withdraw(cantidad)
        destinatario.deposit1(cantidad)

    def accinfo(self):
        print(f"Usuario: {self.name}, Balance: {self.balance}")
        return self

    def money_transf(self, other_user, amount):
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


#accounts

acc1 = BankAcc("ignacio", 1000, 0.01)
acc2 = BankAcc("franco", 1000, 0.01)

#retiros
acc1.make_withdraw(100).make_withdraw(100).make_withdraw(100).deposit1(100).percent()
acc2.make_withdraw(100).make_withdraw(100).deposit1(100).deposit1(100).deposit1(100).deposit1(100).percent()

#account information
acc1.accinfo()
acc2.accinfo()

