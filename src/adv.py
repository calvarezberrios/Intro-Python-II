from room import Room
from player import Player
from item import Item
import os

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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


# Add items to rooms

room["foyer"].items.append(Item("note", "A note from a previous adventurer, it reads: \n        I have slayed the Ogre\n        which dwelled here.\n\n                 Signed\n\n                Black Knight"))
room["overlook"].items.append(Item("sword", "A rusty sword"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Mannie", 100, room["outside"])

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

action = [""]

while action[0].lower() != "q":
    
    print(f"\nYou are in the {player.current_room.name}.\n{player.current_room.description}\n")
    player.current_room.printItems()

    action = input("> ").split(" ")
    verb = action[0].lower()
    obj = ""
    if len(action) > 1: 
        obj = action[1]
    os.system("cls" if os.name == "nt" else "clear")

    if len(action) == 1:
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
                for item in player.current_room.items:
                    if item.name == obj:
                        print(f"\n{item.on_take()}\n")
                        player.inventory.append(item)
                        player.current_room.items.remove(item)
                        break
            else:
                if len(player.current_room.items) < 1:
                    print("\nThere are no items in this room\n")
                else:
                    print(f"\nThere is no {obj} in this room.\n")
        

    
