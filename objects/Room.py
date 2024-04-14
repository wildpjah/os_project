from .Game import Game
class Room():
    name = None
    miner = None
    gamer = None
    gold = 0

    def __init__(self, game, id, name, miner=None, gamer=None, gold=0):
        self.id = id
        self.name = name
        self.miner = miner
        self.gamer = gamer
        self.gold = gold
        self.game = game
    
    def get_id(self):
        return self.id
    def get_name():
        return name
    def get_miner():
        return miner
    def get_gamer():
        return gamer
    def get_gold():
        return gold
    def get_game(self):
        return self.game

    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_miner(self, miner):
        self.miner = miner
    def set_gamer(self, gamer):
        self.gamer = gamer
    def set_gold(self, gold):
        self.id = gold




    def __str__(self):
        output = "Room " + str(self.id) + ", " + str(self.name) + ":"\
            "\nminer in room: " + str(self.miner) + \
            "\ngamer in room: " + str(self.gamer) + \
            "\ngold in room: " + str(self.gold)
        return output

    def __repr__(self):
        output = str(self.name) + ":"\
            "\nminer in room: " + str(self.miner) + \
            "\ngamer in room: " + str(self.gamer) + \
            "\ngold in room: " + str(self.gold)
        return output
