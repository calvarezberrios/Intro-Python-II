from item import Item

class LightSource(Item):
    def __init__(self, name, description, equipped = False):
        super().__init__(name, description)
        self.equipped = equipped

    def on_drop(self):
        return "It's not wise to drop your source of light!\n"