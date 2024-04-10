class Miner:
    name = None
    coins = 0
    in_room = None

    def __init__(self, name, coins, in_room):
        self.name = name
        self.coins = coins
        self.inRoom = in_room

    def __str__(self):
        return self.name + ": {coins:" + str(self.coins) + ", In Room: " + str(self.in_room) + "}"