from .Game import Game
from .Person import Person
import random
class Miner(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)

    def enter_room(self, room):
        if self.room != None:
            self.room.set_miner = None
            self.game.rm_occ_m(self.room)
        self.room = room
        room.set_miner = self
        self.game.add_occ_m(room)
    def find_room(self):
        options = self.game.get_un_occ_m()
        if options[0] == None:
            return None
        r = random.randint(0, len(options)-1)
        return options[r]
    def mine_coins(self):
        r = random.randint(0,5)
        self.add_coins(r)
    def drop_coins(self):
        self.mine_coins()
        self.room.add_coins(self.coins)
        self.set_coins(0)