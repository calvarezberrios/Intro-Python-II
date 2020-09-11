# Implement a class to hold room information. This should have name and
# description attributes.
from lightsource import LightSource

class Room:
    def __init__(self, name, description, items = [], is_light = True):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light

    def printItems(self, player_hasLight):
        if self.is_light == True or self.hasLightSource() == True or player_hasLight == True:
            if len(self.items) > 0:
                print("You can see the following items here:")
                for i, item in enumerate(self.items):
                    print(f"    {i+1}) {item.name.capitalize()}")
                print("")
        else:
            print("It's pitch black! If you have a light source, you should equip it...\n")



    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Room(name: {self.name}, description: {self.description})"

    def hasLightSource(self):
        hasLight = False
        if len(self.items) > 0:
            for item in self.items:
                if isinstance(item, LightSource) == True:
                    hasLight = True
        return hasLight

    def hasItem(self, name):
        found = False
        if len(self.items) > 0:
            for item in self.items:
                if item.name == name:
                    found = True
                    break
            return found
        else:
            return found