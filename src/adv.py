# from room import Room
from player import Player
# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('outside')
command_value = ''

# * Prints the current description (the textwrap module might be useful here).
print('\n\n=========\nWelcome to misterious quest! :D \nHappy hunting!!\n=========\n')
print('Commands: \n n - go north \n s - go south \n e - go east \n w - go west \n q - quit \n\n')
# Write a loop that:
while command_value != 'q':
    # * Prints the current room name
    print(new_player)
    # * Waits for user input and decides what to do.
    command_value = input('What do you want to do? \n<- ')
    # If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if command_value == 'n':
            new_player.go_north()
        elif command_value == 's':
            new_player.go_south()
        elif command_value == 'e':
            new_player.go_east()
        elif command_value == 'w':
            new_player.go_west()
    # Print an error message if the movement isn't allowed.
    except ValueError:
        print('Make sure you are entering right command :)')
# If the user enters "q", quit the game.
print('-> Sad to see you go :( \n   See you next time :)\n')

