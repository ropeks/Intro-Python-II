from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.

room = {
    'outside': Room('outside', 'nothing', 'foyer', 'nothing', 'nothing'),
    'narrow': Room('narrow', 'nothing', 'treasure', 'foyer', 'nothing'),
    'foyer': Room('foyer', 'outside', 'overlook', 'nothing', 'narrow'),
    'treasure': Room('treasure', 'narrow', 'nothing', 'overlook', 'nothing'),
    'overlook': Room('overlook', 'foyer', 'nothing', 'nothing', 'treasure')
}

class Player:
    def __init__(self, room):
        self.room = room
    
    def __str__(self):
        return f'You are currently in room {self.room}'

    def go_north(self):
        north = room[self.room].northworld
        if north != 'nothing':
            print('-> going north!\n\n')
            self.room = north
        else:
            print('-> nothing there..\n\n')

    def go_south(self):
        south = room[self.room].southworld
        if south != 'nothing':
            print('-> going south!\n\n')
            self.room = south
        else:
            print('-> nothing there..\n\n')

    def go_east(self):
        east = room[self.room].eastworld
        if east != 'nothing':
            print('-> going east!\n\n')
            self.room = east
        else:
            print('-> nothing there..\n\n')

    def go_west(self):
        west = room[self.room].westworld
        if west != 'nothing':
            print('-> going west!\n\n')
            self.room = west
        else:
            print('-> nothing there..\n\n')

