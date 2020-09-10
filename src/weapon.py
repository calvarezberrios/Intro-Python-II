from item import Item

class Weapon(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power
        self.equipped = False

    def __str__(self):
        return f"{super().__str__()} - strength modifier: +{self.power}"

    def __repr__(self):
        return f"Item(name: {self.name}, descriptiom: {self.description}, power: {self.power})"