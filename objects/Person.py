class Person:
    def __init__(self, id, name, coins=0, room=None):
        self.id = id
        self.name = name
        self.coins = coins
        self.room = room

    def __repr__(self):
        return type(self).__name__ + " " + str(self.id) + ", " + self.name + ": {coins:" + str(self.coins) + ", In Room: " + str(self.room) + "}"

    def __str__(self):
        return slef.__class__ + " " + str(self.id) + ", " + self.name + ": {coins:" + str(self.coins) + ", In Room: " + str(self.room) + "}"


    def get_name(self):
        return self.name
    def get_Coins(self):
        return self.coins
    def get_room(self):
        return self.room

    def set_name(self, name):
        self.name = name
    def set_coins(self, coins):
        self.coins = coins
    def set_room(self, room):
        self.room = room
    
    
