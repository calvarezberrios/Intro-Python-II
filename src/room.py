# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def printItems(self):
        if len(self.items) > 0:
            print("You can see the following items here:")
            for i, item in enumerate(self.items):
                print(f"    {i+1}) {item.name.capitalize()}")
            print("")

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Room(name: {self.name}, description: {self.description})"

    def hasItem(self, name):
        if len(self.items) > 0:
            for item in self.items:
                if item.name == name:
                    return True
                else:
                    return False
        else:
            return False