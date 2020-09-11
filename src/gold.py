from item import Item

class Gold(Item):
    def __init__(self, name, description, quantity):
        super().__init__(name, description)
        self.value = 1 * quantity
        self.quantity = quantity

    def __str__(self):
        return f"a {super().__str__()} valued at {self.value}G"

    def on_take(self):
        return f"You have picked up {self}"