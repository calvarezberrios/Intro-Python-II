from room import Room
from item import Item
from weapon import Weapon
from gold import Gold

# Create rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, there is a narrow rope bridge across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south."""),
}


# Map out rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Create Items

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