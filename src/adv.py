import os
from room import Room
from player import Player
from item import Item
from weapon import Weapon
from gold import Gold


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Items

sword = Weapon("sword", "A rusty sword", 2)
note = Item("note", """A note from a previous adventurer, it reads: \n
            I have slayed the Ogre
            which dwelled here.
            \n\n                 Signed
            \n\n                 ~Black Knight""")
coinbag = Gold("coinbag", "a bag of 20 gold coins", 20)


# Add items to rooms

room["foyer"].items.append(note)
room["overlook"].items.append(sword)
room["treasure"].items.append(coinbag)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Adventurer", 100, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

os.system("cls" if os.name == "nt" else "clear")

action = [""]

while action[0].lower() != "q":
    
    print(f"Player Name: {player.name} - Health: {player.health} - Gold: {player.gold} - Main Hand: {player.main_hand} - Off Hand: {player.off_hand}")
    print(f"\nYou are in the {player.current_room.name}.\n{player.current_room.description}\n")
    player.current_room.printItems()

    action = input("Type command or 'h / help' for instructions \n> ").split(" ")
    verb = action[0].lower()
    obj = ""

    if len(action) > 1: 
        obj = action[1]

    os.system("cls" if os.name == "nt" else "clear")
    
    if len(action) == 1:
        if verb == "h" or verb == "help":
            with open("help.txt") as helpfile:
                print(helpfile.read())
            input("\nPress [ENTER] to Continue...")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            try:
                if verb == "n":
                    player.current_room = player.current_room.n_to
                elif verb == "s":
                    player.current_room = player.current_room.s_to
                elif verb == "e":
                    player.current_room = player.current_room.e_to
                elif verb == "w":
                    player.current_room = player.current_room.w_to
                elif verb == "i" or verb == "inventory":
                    player.printInventory()
                elif verb == "q":
                    print("\nThank you for playing! Good Bye.\n")
                else:
                    print("\nNot a valid command, please choose: \"n\", \"s\", \"e\", \"w\" \n")
            except:
                print(f"\n***That direction is not allowed from here***\n")
    elif len(action) > 1:
        if verb == "take" or verb == "get":
            if player.current_room.hasItem(obj):
                player.take_item(obj)
            else:
                if len(player.current_room.items) < 1:
                    print("\nThere are no items in this room\n")
                else:
                    print(f"\nThere is no {obj} in this room.\n")
        elif verb == "drop":
            if player.hasItem(obj):
                player.drop_item(obj)
        elif verb == "equip":
            player.equip_weapon(obj)
        elif verb == "unequip":
            player.unequip_weapon(obj)

    
