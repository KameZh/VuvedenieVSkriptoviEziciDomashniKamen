class InventoryManager:
    inventory = {}
    def add_stock(self, quantity, amount):
        if quantity in self.inventory.keys():
            self.inventory[quantity]["available"] += amount
            print(f"Added {amount} to existing stock of {quantity}.")
        else:
            self.inventory[quantity] = {"available": amount,"reserved": 0}
            print(f"Added new stock of {quantity} with amount {amount}.")
    def remove_stock(self, quantity, amount):
        if quantity in self.inventory.keys() and self.inventory[quantity]["available"] >= amount:
            self.inventory[quantity]["available"] -= amount
            print(f"Removed {amount} from stock of {quantity}.")
        else:
            print(f"Insufficient stock or item not found. Item in question: {quantity}")
    def reserve_stock(self, quantity, amount):
        if quantity in self.inventory.keys():
            self.inventory[quantity]["reserved"] += amount
            print(f"Reserved {amount} of {quantity}.")
    def show_stock(self, quantity):
        if quantity == "all":
            print(f"Inventory = {self.inventory}")
        elif quantity in self.inventory.keys(): #moje da se gleda za konkretni produkti
            print(f"Item: {self.inventory[quantity]}")
        else:
            print(f"{quantity} not found in inventory")
    
manager = InventoryManager()
manager.add_stock("apples", 100)
manager.show_stock("all")
manager.add_stock("apples", 20)
manager.show_stock("apples")
manager.add_stock("bananas", 150)
manager.show_stock("all")
manager.remove_stock("nuts", 10)
manager.show_stock("nuts")
manager.remove_stock("apples", 30)
manager.show_stock("all")
manager.reserve_stock("apples", 20)
manager.show_stock("all")