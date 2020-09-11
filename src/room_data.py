from room import Room
from item import Item
from weapon import Weapon
from gold import Gold
from lightsource import LightSource

# Create Items

sword = Weapon("sword", "A rusty sword", 2)
note = Item("note", """A note from a previous adventurer, it reads: \n
            I have slayed the Ogre
            which dwelled here.
            \n\n                 Signed
            \n\n                 ~Black Knight""")
coinbag = Gold("coinbag", "a bag of 20 gold coins", 20)
lamp = LightSource("lamp", "A magically illuminated lamp, must be equipped")



# Create rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [],
                     True),

    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [note],
                     True),

    'overlook': Room("Grand Overlook", 
                     """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, there is a narrow rope bridge across the chasm.""",
                     [sword],
                     True),

    'narrow':   Room("Narrow Passage", 
                     """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [],
                     True),

    'treasure': Room("Treasure Chamber", 
                     """You've found the long-lost treasure
chamber! The only exit is to the south.""",
                     [coinbag, lamp],
                     False),
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



