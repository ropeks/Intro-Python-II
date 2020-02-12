# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room
    
    def __str__(self):
        return f'You are currently in room {self.room}'

    def go_north(self):
        print('-> going north!\n\n')

    def go_south(self):
        print('-> going south!\n\n')

    def go_east(self):
        print('-> going east!\n\n')

    def go_west(self):
        print('-> going west!\n\n')

