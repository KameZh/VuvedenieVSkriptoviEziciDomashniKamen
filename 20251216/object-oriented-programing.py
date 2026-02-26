class Animal: #shablon
#funkcii - narichat se metodi
#moje da se prikachvat i promenlivi
    name=""
    age = 0
    def speak(self):
        print(self.name, self.age)

dog = Animal() # definiciq
cat = Animal()

# ako e osnoven klas moje da ne se slagat skobi

#Nuzdi za izpolzvane na class:

# 1 - Nasledqvane
# edin bazov klas i nasledqvane
class Dog(Animal):
    pass
class Cat(Animal):
    pass

# 2 - Encalsulaciq
class BankAccount:
    name = ""
    balance = ""
    def deposit():
        pass
    def withdraw():
        pass

# 3 - Polimorfizum - iznasqne na funkcionalnostta v drugi klasove
class DOG(Animal):
    def speak(self):
        print("Dzhaf")
class CAT(Animal):
    def speak(self):
        print("Mqu")

# 4 - Abstrakciq - implementaciq


#Izvikvane
a = Animal() # object
b = Animal()
a.name = "Zhiraf"
a.age = 3
a.speak() #-> Zhiraf 3 (nqma nuzda ot parametri, zashtoto e prikachena)
b.speak() #-> _ 0

#vidove funkcii
# 1- Class functions - obvurzani sus samiq fablon
# 2- Object functions - a=Animal()