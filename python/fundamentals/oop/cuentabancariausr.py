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
        