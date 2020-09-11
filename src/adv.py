import os
from room_data import room
from player import Player

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
    player.current_room.printItems(player.hasLight_equipped())

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
            if verb == "n" or verb == "s" or verb == "e" or verb == "w":
                player.move(verb)
            elif verb == "i" or verb == "inventory":
                player.printInventory()
            elif verb == "q":
                print("\nThank you for playing! Good Bye.\n")
            else:
                print("\nNot a valid command\n")
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
            player.equip_item(obj)
        elif verb == "unequip":
            player.unequip_item(obj)

    
