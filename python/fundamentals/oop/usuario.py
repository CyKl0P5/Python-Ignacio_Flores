class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


nacho = User("Adrien")
hayley = User("Mr. Nibbles")
bob = User("Benny Bob")

nacho.make_deposit(100)
nacho.make_deposit(200)
nacho.make_deposit(50)
nacho.make_withdrawl(45)
nacho.display_user_balance()

hayley.make_deposit(1000)
hayley.make_deposit(1000)
hayley.make_withdrawl(500)
hayley.make_withdrawl(300)
hayley.display_user_balance()

bob.make_deposit(1500)
bob.make_withdrawl(1000)
bob.make_withdrawl(5000)
bob.make_withdrawl(3000)
bob.display_user_balance()