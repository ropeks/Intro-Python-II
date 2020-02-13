class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'item name: {0}, descrition: {1}'.format(self.name, self.description)

