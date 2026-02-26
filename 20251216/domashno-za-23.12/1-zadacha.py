import os
class Wallet:
    currency = ""
    balance = 0
    def add_money(self, amount):
        self.balance += amount
        print(f"New Balance after adding money: {self.balance} {self.currency}")
    def spend_money(self, amount):
        if amount > self.balance:
            print("Not enough money")
            return
        self.balance -= amount
        print(f"New Balance after spending money: {self.balance} {self.currency}")
    def show_balance(self):
        print(f"Current Balance: {self.balance} {self.currency}")
    def convert_currency(self, old_currency, new_currency):
        if new_currency == 1:
            new_currency = "BGN"
        elif new_currency == 2:
            new_currency = "USD"
        elif new_currency == 3:
            new_currency = "EUR"

        if old_currency == "BGN" and new_currency == "USD":
            rate = 0.5988
        elif old_currency == "USD" and new_currency == "BGN":
            rate = 1.670
        elif old_currency == "BGN" and new_currency == "EUR":
            rate = 0.5114
        elif old_currency == "EUR" and new_currency == "BGN":
            rate = 1.956
        elif old_currency == "USD" and new_currency == "EUR":
            rate = 0.8540
        elif old_currency == "EUR" and new_currency == "USD":
            rate = 1.171
        elif old_currency == new_currency:
            print("No conversion needed")
            print(f"Balance remains: {self.balance} {self.currency}")
            return
        else:
            print("Conversion rate not available")
            return
        self.balance *= rate
        self.currency = new_currency
        print(f"Balance after conversion: {self.balance} {self.currency}")
    def balance_below(self):
        if self.balance < 0:
            print("Warning: Balance is below zero! Start over and enter a positive balance.")
            exit()
            

profile = Wallet()
os.system('cls')
while profile.currency not in ["BGN", "USD", "EUR", "1", "2", "3"]:
    profile.currency = input("Enter currency type (BGN, USD, EUR): ")
    if profile.currency == "1":
        profile.currency = "BGN"
        print(profile.currency)
    elif profile.currency == "2":
        profile.currency = "USD"
        print(profile.currency)
    elif profile.currency == "3":
        profile.currency = "EUR"
        print(profile.currency)
profile.balance = int(input("Enter starting amount: "))
profile.balance_below()
while True:
    os.system('cls')
    profile.show_balance()
    print("===================================")
    action = input("Would you like to add money(a), spend money (s), show balance(b), convert currency(cc), or exit(ext)? ").lower()
    if action == "add money" or action == "a":
        os.system('cls')
        profile.show_balance()
        profile.add_money(int(input("Enter amount to add: ")))
    elif action == "spend money" or action == "s":
        os.system('cls')
        profile.show_balance()
        profile.spend_money(int(input("Enter amount to spend: ")))
        profile.balance_below()
    elif action == "show balance" or action == "b":
        os.system('cls')
        profile.show_balance()
    elif action == "convert currency" or action == "cc":
        os.system('cls')
        new_currency = input("Enter currency to convert to (BGN, USD, EUR): ")
        profile.convert_currency(profile.currency, new_currency)
    elif action == "exit" or action == "ext":
        os.system('cls')
        print("Exiting the wallet system.")
        break
    else:
        print("Invalid action. Please choose add money, spend money, show balance, convert currency, or exit.")