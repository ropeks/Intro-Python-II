from player import Player

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('outside')
command_value = ''

# * Prints the current description (the textwrap module might be useful here).
print('\n\n=========\nWelcome to misterious quest! :D \nHappy hunting!!\n=========\n')
print('Commands: \n n  - go north \n s  - go south \n e  - go east \n w  - go west \n sr - search for items in current room \n q  - quit \n\n')
# Write a loop that:
while command_value != 'q':
    # * Prints the current room name
    print(new_player)
    # * Waits for user input and decides what to do.
    command_value = input('What do you want to do? \n<- ')
    # If the user enters a cardinal direction, attempt to move to the room there.
    if command_value == 'n':
        new_player.go_north()
    elif command_value == 's':
        new_player.go_south()
    elif command_value == 'e':
        new_player.go_east()
    elif command_value == 'w':
        new_player.go_west()
    elif command_value == 'sr':
        new_player.search_room()
    # Print an error message if the movement isn't allowed.
    elif command_value != 'q':
        print('-> Make sure you are entering the right command :)\n\n')
# If the user enters "q", quit the game.
print('-> Sad to see you go :( \n   See you next time :)\n\n')

