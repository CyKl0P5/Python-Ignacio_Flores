from colorama import Fore,Style

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

class Capybara(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 90
        self.happiness = 100
        self.specie = "Capybara"

    def PI(self):
        super().PIA()
        print(Fore.CYAN + "Health" + Style.RESET_ALL, self.health)
        print(Fore.CYAN + "Happiness" + Style.RESET_ALL, self.happiness)
        print(Fore.CYAN + "Specie" + Style.RESET_ALL, self.specie)
        print(Fore.RED + "------------------------------------" + Style.RESET_ALL)
        return self

    def feed(self):
        if self.health != 100:
            print(f"Se ha alimentado a {self.name}")
            self.health += 10
        else:
            print(f"No se puede seguir alimentando a {self.name}")
        return self

class Penguin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 30
        self.happiness = 70
        self.specie = "Penguin"

    def PI(self):
        super().PIA()
        print(Fore.CYAN + "Health" + Style.RESET_ALL, self.health)
        print(Fore.CYAN + "Happiness" + Style.RESET_ALL, self.happiness)
        print(Fore.CYAN + "Specie" + Style.RESET_ALL, self.specie)
        print(Fore.RED + "------------------------------------" + Style.RESET_ALL)
        return self

    def feed(self):
        if self.health != 100:
            print(f"Se ha alimentado a {self.name}")
            self.health += 10
        else:
            print(f"No se puede seguir alimentando a {self.name}")
        return self

class Zoo:
    def __init__(self,name):
        self.name = name
        self.animals = []

    def AG(self,name):
        self.animals.append(Cat(name, 4))
        return self
    
    def AC(self,name):
        self.animals.append(Capybara(name, 5))
        return self
    
    def AP(self,name):
        self.animals.append(Penguin(name, 1))
        return self

    def PrintInfo(self):
        print(Fore.YELLOW+ "-"*30,self.name,"-"*30+ Style.RESET_ALL)
        for anim in self.animals:
            anim.PI()
        return self

Zoo1 = Zoo("ZOOKEE")

Zoo1.AG("Cat").AC("Capyto").AP("Mumble").PrintInfo()