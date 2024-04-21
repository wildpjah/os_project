from .Game import Game
from .Person import Person
import random
import asyncio
class Gamer(Person):
    def __init__(self, game, id, name, coins=0, room=None,):
        super().__init__(game, id, name, coins, room)
        self.time = 10
        self.lock = asyncio.Lock()

    async def enter_room(self, room):
        async with self.lock:
            old_room = self.room
            if self.room != None:
                self.leave_room()
            if room is None:
                pass
            else:
                self.room = room
                room.set_gamer(self)
                self.game.add_occ_g(room)
                self.game.rm_un_occ_g(room)
                asyncio.sleep(1/100)

    def find_room(self):
        un_occ = self.game.get_un_occ_g()
        level = self.game.level_from_gamer(self)
        rooms = (level).get_rooms()
        options = []
        for room in rooms:
            if room in un_occ:
                options.append(room)
        if options == []:
            return None
        r = random.randint(0, len(options)-1)
        return options[r]
    async def collect(self):
        async with self.lock:
            r = self.room
            delay = 0
            if self.room != None:
                c = self.room.get_coins()
                if c <=10:
                    self.add_coins(c)
                    r.set_coins(0)
                    delay = c
                else:
                    c = 10
                    self.add_coins(10)
                    delay = 10
                    r.set_coins(c-10)
            asyncio.sleep(delay/100)

    async def leave_room(self):
        async with self.lock:
            r = self.room
            r.set_gamer(None)
            self.game.rm_occ_g(r)
            self.game.add_un_occ_g(r)
            self.room = None
            asyncio.sleep(1/100)


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
                level_gamers.remove(self)
                level.set_gamers(level_gamers)
                i = all_levels.index(level)
                new_level = all_levels[i+1]
                level_gamers = new_level.get_gamers()
                level_gamers.append(self)
                new_level.set_gamers(level_gamers)
                print("Gamer" + str(self.get_id()) + " Leveled up! Is now Level " + str(new_level.get_id()))



    async def loop_for_t(self, t):
        async with self.lock:
            print("GAMER loop start *************************************")
            i=0
            start = 0
            end = 0
            change = 0
            await asyncio.sleep(2)
            while(self.game.check_win() == False and i<t):
                await asyncio.sleep(0)
                print("Gamer " + str(self.get_id()) + " execution " + str(i) + " START")
                start = self.coins
                await self.enter_room(self.find_room())
                await self.collect()
                end = self.coins
                self.level_up()
                i = i + 1
                change = end-start
                #Note that change is before level-up
                print("Gamer " + str(self.get_id()) + " execution " + str(i) + ". Gained " + str(change) + " coins")
            print("GAMER loop end *****************************")
            print(i)

    async def loop_for_win(self):
        async with self.lock:
            await asyncio.sleep(2)
            while(self.game.check_win() == False):
                await asyncio.sleep(0)
                await self.enter_room(self.find_room())
                await self.collect()
                self.level_up()

    async def loop_one(self):
        async with self.lock:
            await asyncio.sleep(0)
            await self.enter_room(self.find_room())
            await self.collect()
            self.level_up()