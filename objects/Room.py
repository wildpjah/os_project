class Room:
    name = None
    miner = None
    gamer = None
    gold = 0

    def __init__(self, name, miner, gamer, gold):
        self.name = name
        self.miner = miner
        self.gamer = gamer
        self.gold = gold

    def __str__(self):
        output = str(self.name) + ":"\
            "\nminer in room: " + str(self.miner) + \
            "\ngamer in room: " + str(self.gamer) + \
            "\ngold in room: " + str(self.gold)
        return output
