from .Game import Game
class Room():

    def __init__(self, game, id, name, miner=None, gamer=None, coins=0):
        self.id = id
        self.name = name
        self.miner = miner
        self.gamer = gamer
        self.coins = coins
        self.game = game
    
    def get_id(self):
        return self.id
    def get_name():
        return self.name
    def get_miner():
        return self.miner
    def get_gamer():
        return self.gamer
    def get_coins():
        return self.coins
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
    def set_coins(self, coins):
        self.coins = coins

    def add_coins(self, coins):
        self.coins += coins


    def __str__(self):
        output = "Room " + str(self.id) + ", " + str(self.name) + ":"\
            "\nminer in room: " + str(self.miner) + \
            "\ngamer in room: " + str(self.gamer) + \
            "\ngold in room: " + str(self.coins)
        return output

    def __repr__(self):
        output = str(self.name) + ":"\
            "\nminer in room: " + str(self.miner) + \
            "\ngamer in room: " + str(self.gamer) + \
            "\ngold in room: " + str(self.coins)
        return output
