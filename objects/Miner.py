from .Game import Game
from .Person import Person
import random
import time
class Miner(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)

    # def enter_room(self, room):
    #     if self.room != None:
    #         self.room.set_miner = None
    #         self.game.rm_occ_m(self.room)
    #     self.room = room
    #     room.set_miner(self)
    #     self.game.add_occ_m(room)
    # def find_room(self):
    #     options = self.game.get_un_occ_m()
    #     if options[0] == None:
    #         return None
    #     r = random.randint(0, len(options)-1)
    #     return options[r]

    def enter_room(self, room):
        old_room = self.room
        if self.room != None:
            self.leave_room()
        self.room = room
        room.set_miner(self)
        self.game.add_occ_m(room)
    def find_room(self):
        options = self.game.get_un_occ_m()
        if options == None:
            return None
        r = random.randint(0, len(options)-1)
        return options[r]
    def leave_room(self):
        r = self.room
        r.set_miner(None)
        self.game.rm_occ_m(r)
        self.room = None


    def mine_coins(self):
        r = random.randint(0,5)
        self.add_coins(r)
    def drop_coins(self):
        self.mine_coins()
        self.room.add_coins(self.coins)
        self.set_coins(0)


    def loop_for_t(self, t):
        i=0
        while(self.game.check_win() == False and i<t):
            self.enter_room(self.find_room())
            self.drop_coins()
            i = i + 1
    
    def loop_for_win(self):
        while(self.game.check_win() == False):
            print("m")
            self.enter_room(self.find_room())
            self.drop_coins()

    def loop_one(self):
        print(self)
        self.enter_room(self.find_room())
        self.drop_coins()