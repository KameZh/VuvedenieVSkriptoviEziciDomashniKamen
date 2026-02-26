class BankAccount:
    name = ""
    balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"New Balance after deposit: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
            return
        self.balance -= amount
        print(f"New Balance after withdraw: {self.balance}")
    def __init__(self, name="", balance=0): #oshte edin metod sushtiq kato drugiq - konstruktor
        self.name = name
        self.balance = balance
        
axl = BankAccount()
axl.name = "Axl Rose"
axl.deposit(200)
axl.withdraw(35)

slash = BankAccount()
slash.name = "Saul Hudson"
slash.deposit(1000)
slash.withdraw(1500)

ivan = BankAccount("Ivan", 200)
ivan.withdraw(400)