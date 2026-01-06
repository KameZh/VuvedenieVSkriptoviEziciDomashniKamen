class Player:
    name = ""
    health = 0
    energy = 0

    def attack(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} attacks! Energy left: {self.energy}")
        else:
            print(f"{self.name} does not have enough energy to attack.")
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
            return None
        print(f"{self.name} takes {damage} damage! Health left: {self.health}")
    def heal(self, amount):
        hp = self.health
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name} heals for {amount}! Health now: {self.health}")
        if hp + amount > 100:
            wasted = hp + amount - 100
            print(f"Excess healing wasted {wasted}HP")
    def status(self):
        print(f"Player: {self.name}, Health: {self.health}, Energy: {self.energy}")
    def __init__(self, name="", health=100, energy=100):
        self.name = name
        self.health = health
        self.energy = energy

player1 = Player("Hero", 100, 100)
player1.status()
while player1.energy:
    player1.attack()
player1.take_damage(30)
player1.heal(50)
while player1.health:
    player1.take_damage(15)
