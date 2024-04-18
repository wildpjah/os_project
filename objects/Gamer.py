from .Game import Game
from .Person import Person
import random
import time
import asyncio
class Gamer(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)

    def enter_room(self, room):
        old_room = self.room
        if self.room != None:
            self.leave_room()
        self.room = room
        room.set_gamer(self)
        self.game.add_occ_g(room)
    def find_room(self):
        un_occ = self.game.get_un_occ_g()
        level = self.game.level_from_gamer(self)
        rooms = (level).get_rooms()
        options = []
        for room in rooms:
            if room in un_occ:
                options.append(room)
        if options[0] == None:
            return None
        r = random.randint(0, len(options)-1)
        return options[r]
    def collect(self):
        r = self.room
        if self.room != None:
            self.add_coins(self.room.get_coins())
            r.set_coins(0)
    def leave_room(self):
        r = self.room
        r.set_gamer(None)
        self.game.rm_occ_g(r)
        self.room = None


    def level_up(self):
        # check for level up condition
        g = self.game
        if self.coins >= 20:
            # did we just win the last level?
            level = g.level_from_gamer(self)
            all_levels = g.get_levels()
            num_l = len(g.get_levels())
            if level == all_levels[num_l-1]:
                self.game.win(self)
            else:
                # level up
                self.coins = 0
                if self.room != None:
                    self.leave_room()
                level_gamers = level.get_gamers()
                new_level_gamers = level_gamers.remove(self)
                level.set_gamers(new_level_gamers)
                i = all_levels.index(level)
                new_level = all_levels[i+1]
                level_gamers = new_level.get_gamers()
                level_gamers.append(self)
                new_level.set_gamers(level_gamers)



    async def loop_for_t(self, t):
        print("GAMER loop start *************************************")
        i=0
        while(self.game.check_win() == False and i<t):
            await asyncio.sleep(0)
            self.enter_room(self.find_room())
            self.collect()
            self.level_up()
            i = i + 1
            print("GAMER execution" + str(i))
        print("GAMER loop end *****************************")
        print(i)

    def loop_for_win(self):
        while(self.game.check_win() == False):
            print("gamer")
            self.enter_room(self.find_room())
            self.collect()
            self.level_up()

    def loop_one(self):
        print("gamer")
        self.enter_room(self.find_room())
        self.collect()
        self.level_up()