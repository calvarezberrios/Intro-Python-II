# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, health, current_room):
        self.name = name
        self.health = health
        self.current_room = current_room
        self.inventory = []

    def printInventory(self):
        print("\n---------------------------------------------\n")
        print(f"   {self.name.capitalize()}'s Inventory:\n")
        if len(self.inventory) > 0:
            for i, item in enumerate(self.inventory):
                print(f"   {i + 1}) {item.name.capitalize()} - {item.description}\n")
        else:
            print("   You have no item in your inventory... :(")
        print("\n---------------------------------------------\n")


    def __str__(self):
        return f"{self.name.capitalize()} has health {self.health} and is currently in room {self.current_room}"

    def __repr__(self):
        return f"Player(health: {self.health}, room: {self.current_room})"
