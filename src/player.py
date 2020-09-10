# Write a class to hold player information, e.g. what room they are in
# currently.
from gold import Gold
from weapon import Weapon
class Player:
    def __init__(self, name, health, current_room):
        self.name = name
        self.health = health
        self.current_room = current_room
        self.inventory = []
        self.strength = 1
        self.armor = 0
        self.main_hand = "empty"
        self.off_hand = "empty"
        self.gold = 0

    def printInventory(self):
        print("\n---------------------------------------------\n")
        print(f"   {self.name.capitalize()}'s Inventory:\n")
        if len(self.inventory) > 0:
            for i, item in enumerate(self.inventory):
                print(f"   {i + 1}) {item}\n")
        else:
            print("   You have no item in your inventory... :(")
        print("\n---------------------------------------------\n")


    def __str__(self):
        return f"{self.name.capitalize()} has health {self.health} and is currently in room {self.current_room}"

    def __repr__(self):
        return f"Player(health: {self.health}, room: {self.current_room})"

    def hasItem(self, name):
        found = False
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.name == name:
                    found = True
                    break
            return found
        else:
            return found

    def equip_weapon(self, weapon):
        if self.hasItem(weapon):
            for item in self.inventory:
                if item.name == weapon and isinstance(item, Weapon) == True:
                    self.main_hand = item.name.capitalize()
                    self.strength = 1 + item.power
                    item.equipped = True
                    print(f"{item.name.capitalize()} has been equipped\n")
                    break
                elif item.name == weapon and isinstance(item, Weapon) == False:
                    print(f"The {item.name} is not a weapon")
                    break
        else:
            print(f"You do not have a {weapon}\n")

    def unequip_weapon(self, weapon):
        if self.hasItem(weapon):
            for item in self.inventory:
                if item.name == weapon and isinstance(item, Weapon) == True:
                    self.main_hand = "empty"
                    self.strength = 1
                    item.equipped = False
                    print(f"{item.name.capitalize()} has been unequipped\n")
                    break
                elif item.name == weapon and isinstance(item, Weapon) == True:
                    print(f"You do not have a {weapon} equipped")
                    break
                elif item.name == weapon and isinstance(item, Weapon) == False:
                    print(f"The {weapon} is not a weapon, therefore it's not equipped")
                    break
        else:
            print(f"You do not have a {weapon}\n")

    def hold_item(self, item):
        self.off_hand = item
        if item.name.lower() == "shield":
            self.armor += item.defense

    def take_item(self, obj):
        for item in self.current_room.items:
            if item.name == obj:
                print(f"\n{item.on_take()}\n")
                if isinstance(item, Gold):
                    self.gold += item.value
                    self.current_room.items.remove(item)
                else:
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                break
    
    def drop_item(self, obj):
        if self.hasItem(obj) == True:
            for item in self.inventory:
                if item.name == obj and isinstance(item, Weapon) == True and item.equipped == True:
                    print(f"You must unequip the {obj} first before dropping it")
                    break
                elif item.name == obj:
                    print(item.on_drop())
                    self.current_room.items.append(item)
                    self.inventory.remove(item)
                    break
        else:
            print(f"You do not have a {obj}")
