from colorama import Fore, Style

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PIA(self):
        print(Fore.GREEN + f"==========Info self.name=========="+ Style.RESET_ALL)
        print(Fore.CYAN + "Name:"+ Style.RESET_ALL + self.name)
        print(Fore.CYAN + "Age:" + Style.RESET_ALL + str(self.age))

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 60
        self.happiness = 50
        self.specie = "Cat"

    def PI(self):
        super().PIA()
        print(Fore.CYAN + "Health" + Style.RESET_ALL, self.health)
        print(Fore.CYAN + "Happiness" + Style.RESET_ALL, self.happiness)
        print(Fore.CYAN + "Specie" + Style.RESET_ALL, self.specie)
        print(Fore.RED + "------------------------------------" + Style.RESET_ALL)
        return self