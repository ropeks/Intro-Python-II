# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, northworld, southworld, eastworld, westworld):
        self.name = name
        self.northworld = northworld
        self.southworld = southworld
        self.eastworld = eastworld
        self.westworld = westworld

    def __str__(self):
        return 'name: {0}, northworld: {1}, southworld: {2}, eastworld: {3}, westworld: {4}'.format(self.name, self.northworld, self.southworld, self.eastworld, self.westworld)

