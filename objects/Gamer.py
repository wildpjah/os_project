from .Game import Game
from .Person import Person
import random
import asyncio
import sys
from .GameChangeEvent import GameChangeEvent
import time

class Gamer(Person):
    def __init__(self, game, id, name, coins=0, level=0, room=None):
        super().__init__(game, id, name, coins, level, room)
        self.TIME = 50

    async def enter_room(self, room):
        old_room = self.room
        if old_room == room:
            pass
        if self.room != None:
            await self.leave_room()
        if room is None:
            pass
        else:
            if room not in self.game.un_occ_g:
                pass
            self.room = room
            room.set_gamer(self)
            self.game.add_occ_g(room)
            if room not in self.game.un_occ_g:
                pass
            self.game.rm_un_occ_g(room)
            await asyncio.sleep(self.TIME*1/100)

    def find_room(self):
        un_occ = self.game.get_un_occ_g()
        level = self.level
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
        r = self.room
        delay = 0
        if self.room != None:
            c = r.get_coins()
            if c <=10:
                self.add_coins(c)
                r.set_coins(0)
                delay = c
            else:
                self.add_coins(10)
                delay = 10
                r.set_coins(c-10)
        start = time.time()
        await asyncio.sleep(self.TIME*delay/100)
        end = time.time()
        sys.stdout.write("Gamer " + str(self.get_id()) + " execution COLLECT waited " + str(end-start) + " seconds\n")

    async def leave_room(self):
        r = self.room
        r.set_gamer(None)
        self.game.rm_occ_g(r)
        self.game.add_un_occ_g(r)
        self.room = None
        await asyncio.sleep(self.TIME*1/100)


    def level_up(self):
        # check for level up condition
        g = self.game
        if self.coins >= 20:
            # did we just win the last level?
            level = self.level
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
                self.level=new_level
                print("Gamer" + str(self.get_id()) + " Leveled up! Is now Level " + str(new_level.get_id()))



    async def loop_for_t(self, t):
        await asyncio.sleep(2)
        sys.stdout.write("GAMER loop start *************************************\n")
        i=0
        start = 0
        end = 0
        change = 0
        while(self.game.check_win() == False and i<t):
            await asyncio.sleep(0)
            sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + " START\n")
            start = self.coins
            r = self.find_room()
            # Each of these functions is locked individually, but the next one aquires the lock immediately after releasing it
            # This keeps each room locked as long as the gamer is in it
            if r is not None:
                async with r.get_g_lock():
                    sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + " LOCK\n")
                    self.game.notify_observers()
                    await self.enter_room(r)
                    sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + " ENTER\n")
                    self.game.notify_observers()
                    await self.collect()
                    sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + " COLLECT\n")
                    self.game.notify_observers()
                    await self.leave_room()
                    sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + " LEAVE\n")
                    self.game.notify_observers()
                end = self.coins
                self.level_up()
                sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + " LEVEL UP CHECK\n")
                self.game.notify_observers()
                change = end-start
                #Note that change is before level-up
                sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + ". Gained " + str(change) + " coins\n")
                await asyncio.sleep(.5)
            else:
                sys.stdout.write("Gamer " + str(self.get_id()) + " execution " + str(i) + ": No empty room, execution skipped\n")
            i = i + 1
        sys.stdout.write("GAMER loop end *****************************\n")
        sys.stdout.write(str(i) + "\n")

    async def loop_for_win(self):
        await asyncio.sleep(self.TIME*2)
        while(self.game.check_win() == False):
            room = self.find_room()
            if room is not None:
                async with room.get_g_lock():
                    await self.enter_room(room)
                    await self.collect()
                    await self.leave_room()
            await asyncio.sleep(self.TIME*.5)
            self.level_up()

    async def loop_one(self):
        await asyncio.sleep(self.TIME*2)
        await asyncio.sleep(self.TIME*0)
        room = self.find_room()
        if room is not None:
            async with room.get_g_lock():
                await self.enter_room(room)
                await self.collect()
                await self.leave_room()
        await asyncio.sleep(self.TIME*.5)
        self.level_up()