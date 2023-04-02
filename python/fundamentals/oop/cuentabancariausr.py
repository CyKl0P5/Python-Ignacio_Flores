#accounts
class accs:
    def __init__(self, num_acc, usr, amount):
        self.num_acc = num_acc
        self.usr = usr
        self.balance = amount

    def Alook(self, num_acc):
        if num_acc == self.num_acc:
            return True
        else:
            return False
        
    def __str__(self):
        return f"La cuenta {self.num_acc} es de {self.usr.name} y su saldo es {self.balance}"
    

#user
class user:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.accounts = []

    def Ulook(self, name):
        if name == self.name:
            return True
        else:
            return False

    def addAcc(self, account):
        self.accounts.append(account)
        print(f"Cuenta {account.num_acc} agregada")
        print("----------------")

    def deposit(self, num_acc, amount):
        for account in self.accounts:
            if account.Alook(num_acc):
                account.balance += amount
                print(f"Se ha Depositado {amount} en la cuenta {account.num_acc}")
                print(account)
                print("--------------")
                return self
            print(f"La cuenta no existe {num_acc}")
    

    def withdraw(self, num_acc, amount):
        for account in self.accounts:
            if account.Alook(num_acc):
                account.balance -= amount
                print(f"Se retiro {amount} en la cuenta {account.num_acc}")
                print(account)
                print("-------------")
                return self
            print(f"La cuenta no existe {num_acc}")

    def balance(self, num_acc):
        for account in self.accounts:
            if account.Alook(num_acc):
                print(f"El saldo actual de la cuenta {account.num_acc} es {acc.balance}")
                print("----------")
                return self
            print(f"La cuenta no existe {num_acc}")

    def info_acc(self):
        print(f"Usr: {self.name}, {accounts.self.num_acc} Balance: {accounts.self.balance}")

    def moneytr(self, other_Usr, acc_origin, acc_destiny, amount):
        for account in self.accounts:
            if account.Alook(acc_origin.num_acc):
                for account_other_usr in other_Usr.accounts:
                    if account_other_Usr.Alook(acc_destiny.num_acc):
                        account.balance -= amount
                        account_other_Usr.balance += amount
                        print("Transaccion completada")
                        print(account)
                        print(account_other_Usr)
                        print("----------")
                        return self
            print(f"No existe la cuenta {acc_origin.num_acc} o la cuenta {acc_destiny.num_acc}")


#users
Usr1 = User("nacho", 1000)
Usr2 = User("leon", 0)

#accounts
acc1 = accounts("001", Usr1, Usr1.amount)
acc2 = accounts("002", Usr2, Usr2.amount)
acc3 = accounts("003", Usr1, Usr1.amount)

#user 1
if Usr1.Ulook("nacho") == true:
    print("Hola!" + Usr1.name + ", gracias por prefererirnos!!! aqui estan tus cuentas nuevas")
    Usr1.addacc(acc1)
    Usr1.addacc(acc3)

#user 2
if Usr2.Ulook("leon") == true:
    print("Hola!" + Usr2.name + ", gracias por prefererirnos!!! aqui estan tus cuentas nuevas")
    Usr2.addacc(acc2)

#deposit
Usr1.deposit("001", 900000)

#money transf
Usr1.moneytr(Usr2, acc1, acc2, 100000).moneytr(
    Usr1, acc1, acc3, 1000)

#balance check
Usr2.balance("002")

#withdraw money
Usr2.withdraw("002", 1000)

#info
Usr1.acc_info()