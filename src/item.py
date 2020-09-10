class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name.capitalize()} - {self.description}"

    def __repr__(self):
        return f"Item(name: {self.name}, descriptiom: {self.description})"

    def on_take(self):
        return f"You have picked up {self.name}"

    def on_drop(self):
        return f"You have dropped {self.name}"
        