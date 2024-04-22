from .Game import Game
import asyncio
class Room():

    def __init__(self, game, id, name, miner=None, gamer=None, coins=0):
        self.id = id
        self.name = name
        self.miner = miner
        self.gamer = gamer
        self.coins = coins
        self.game = game
        self.m_lock = asyncio.Lock()
        self.g_lock = asyncio.Lock()
    
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_miner(self):
        return self.miner
    def get_gamer(self):
        return self.gamer
    def get_coins(self):
        return self.coins
    def get_game(self):
        return self.game
    def get_m_lock(self):
        return self.m_lock
    def get_g_lock(self):
        return self.g_lock

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
        m_name = ""
        g_name = ""
        if self.miner != None:
            m_name = self.miner.get_name()
        if self.gamer != None:
            g_name = self.gamer.get_name()
        output = "Room " + str(self.id) + ", " + str(self.name) + ":"\
            "\nminer in room: " + str(m_name) + \
            "\ngamer in room: " + str(g_name) + \
            "\ncoins in room: " + str(self.coins)
        return output

    def __repr__(self):
        m_name = ""
        g_name = ""
        if self.miner != None:
            m_name = self.miner.get_name()
        if self.gamer != None:
            g_name = self.gamer.get_name()
        output = str(self.name) + ":"\
            "\nminer in room: " + str(m_name) + \
            "\ngamer in room: " + str(m_name) + \
            "\ncoins in room: " + str(self.coins)
        return output
