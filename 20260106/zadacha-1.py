class OnlineShopAccount:
    username = ""
    balance = 0.0
    items = []
    def add_funds(self, amount):
        self.balance += amount
    def buy_item(self, item_name, price):
        if self.balance >= price:
            self.items.append({
                "name": item_name,
                "price": price
            })
            self.balance -= price
            print(f"Item purchased: {item_name} for {price}.")
        elif self.balance < price:
            print(f"Unsefficient funds to complete the purchase of {item_name}.")
    def refund(self, item_name):
        found = 0
        for index, item in enumerate(self.items):
            if item_name == item.get("name"):
                self.balance += item.get("price")
                found = 1
        if found:
            print(f"Item refunded {item_name}.")
            self.items.pop(index)
        else:
            print(f"No record of '{item_name}' purchase found for refund.")
    def show_balance(self):
        print(f"{self.username}'s current balance is {self.balance}.")
    def __init__(self, username="", balance=0.0):
        self.username = username
        self.balance = balance
        self.items = []

User1 = OnlineShopAccount("Pesho", 5000)
User1.show_balance()
User1.buy_item("Laptop", 3200)
User1.show_balance()
User1.buy_item("Smartphone", 1900)
User1.show_balance()
User1.refund("Soup")
User1.refund("Laptop")
User1.show_balance()
User1.buy_item("Smartphone", 1900)
User1.show_balance()
