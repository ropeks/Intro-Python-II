from room import Room
from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.

room = {
    'outside': Room('outside', 'nothing', 'foyer', 'nothing', 'nothing', [Item('knife', 'a dangerous weapon')]),
    'narrow': Room('narrow', 'nothing', 'treasure', 'foyer', 'nothing', [ Item('image', 'there is a woman on it'), Item('bag', 'just an empty bag..') ]),
    'foyer': Room('foyer', 'outside', 'overlook', 'nothing', 'narrow', []),
    'treasure': Room('treasure', 'narrow', 'nothing', 'overlook', 'nothing', [Item('treasure', 'hidden treasure')]),
    'overlook': Room('overlook', 'foyer', 'nothing', 'nothing', 'treasure', [])
}

class Player:
    def __init__(self, room, inventory = []):
        self.room = room
        self.inventory = inventory
    
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

    def search_room(self):
        current_room_items = room[self.room].items

        if len(current_room_items) > 0:

            print('-> Items:')
            for item in current_room_items:
                print('  - ' + item.name)
            print('\n')

            command_value = ''
            while command_value != 'b':
                command_value = input("Type item name to pick up the item or 'b' to go back \n<- ")
                
                if command_value != 'b':
                    try:
                        i = 0
                        number_of_items = len(current_room_items)
                        while i != number_of_items:
                            if current_room_items[i].name == command_value:
                                print(f'-> Picking up {command_value}')
                                self.inventory.append(current_room_items[i])
                                current_room_items.pop(i)
                            i += 1
                        print('-> Items left: ')
                        for item in current_room_items:
                            print('  - ' + item.name)
                        print('\n')
                    except:
                        print('-> Make sure you are passing right command!\n\n')
            
            print('-> Going back \n\n')
    
        else:
            print('-> Looks like someone has already looted everything here :( \n\n')

    def get_inventory(self):
        if len(self.inventory) > 0:

            print('-> Inventory: ')
            for item in self.inventory:
                print('  - ' + item.name)
            print('\n')

            command_value = ''
            while command_value != 'b':
                command_value = input("Type item name to drop the item or 'b' to go back \n<- ")
                
                if command_value != 'b':
                    # try:
                        i = 0
                        number_of_items = len(self.inventory)
                        while i != number_of_items:
                            if self.inventory[i-1].name == command_value:
                                print(f'-> Dropping {command_value}')
                                room[self.room].items.append(self.inventory[i])
                                self.inventory.pop(i)
                            i += 1
                        print('-> Inventory: ')
                        for item in self.inventory:
                            print('  - ' + item.name)
                        print('\n')
                    # except:
                    #     print('-> Make sure you are passing right command!\n\n')
            
            print('-> Going back \n\n')
        else:
            print('-> Your inventory is empty.\n\n')


