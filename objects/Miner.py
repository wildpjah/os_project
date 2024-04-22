from .Game import Game
from .Person import Person
import random
import asyncio
import sys

class Miner(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)


    async def enter_room(self, room):
        old_room = self.room
        if self.room != None:
            await self.leave_room()
        if room is None:
            pass
        else:
            async with room.get_m_lock():
                self.room = room
                room.set_miner(self)
                self.game.add_occ_m(room)
                self.game.rm_un_occ_m(room)
                await asyncio.sleep(1/100)
    def find_room(self):
        options = self.game.get_un_occ_m()
        if options == []:
            return None
        r = random.randint(0, len(options)-1)
        return options[r]
    async def leave_room(self):
        async with self.room.get_m_lock():
            r = self.room
            r.set_miner(None)
            self.game.rm_occ_m(r)
            self.game.add_un_occ_m(r)
            self.room = None
            await asyncio.sleep(1/100)


    def mine_coins(self):
        r = random.randint(0,5)
        self.add_coins(r)
    async def drop_coins(self):
        async with self.room.get_m_lock():
            self.mine_coins()
            self.room.add_coins(self.coins)
            self.set_coins(0)
            await asyncio.sleep(self.get_coins()/1000)


    async def loop_for_t(self, t):
        sys.stdout.write("miner loop start *************************************\n")
        i=0
        start = 0
        end = 0
        change = 0
        while(self.game.check_win() == False and i<t):
            i = i + 1
            await asyncio.sleep(0)
            sys.stdout.write("Miner " + str(self.get_id()) + " execution " + str(i) + " START\n")
            room = self.find_room()
            if room is not None:
                start = room.get_coins()
                await self.enter_room(room)
                await self.drop_coins()
                await self.leave_room()
                end = room.get_coins()
                change = end-start
                sys.stdout.write("Miner " + str(self.get_id()) + " execution " + str(i) + ". Dropped " + str(change) + " coins in Level: " + str(self.game.level_from_room(room).get_id()) + " Room: " + str(room.get_id()) + "\n")
                await asyncio.sleep(.5)
            else:
                sys.stdout.write("Miner " + str(self.get_id()) + " execution " + str(i) + ": No empty room, execution skipped\n")
            
        sys.stdout.write("miner loop end *****************************\n")
        sys.stdout.write(str(i) + "\n")
    
    async def loop_for_win(self):
        while(self.game.check_win() == False):
            room = self.find_room()
            if room is not None:
                await self.enter_room(room)
                await self.drop_coins()
                await self.leave_room()
            await asyncio.sleep(.5)

    async def loop_one(self):
        await self.enter_room(self.find_room())
        await self.drop_coins()