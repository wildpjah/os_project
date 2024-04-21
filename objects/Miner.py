from .Game import Game
from .Person import Person
import random
import asyncio
class Miner(Person):
    def __init__(self, game, id, name, coins=0, room=None):
        super().__init__(game, id, name, coins, room)
        self.lock = asyncio.Lock()


    async def enter_room(self, room):
        async with self.lock:
            old_room = self.room
            if self.room != None:
                await self.leave_room()
            if room is None:
                pass
            else:
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
        async with self.lock:
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
        async with self.lock:
            self.mine_coins()
            self.room.add_coins(self.coins)
            self.set_coins(0)
            await asyncio.sleep(self.get_coins()/1000)


    async def loop_for_t(self, t):
        async with self.lock:
            print("miner loop start *************************************")
            i=0
            start = 0
            end = 0
            change = 0
            while(self.game.check_win() == False and i<t):
                i = i + 1
                await asyncio.sleep(0)
                print("Miner " + str(self.get_id()) + " execution " + str(i) + " START")
                room = self.find_room()
                start = room.get_coins()
                await self.enter_room(room)
                await self.drop_coins()
                end = room.get_coins()
                change = end-start
                print("Miner " + str(self.get_id()) + " execution " + str(i) + ". Dropped " + str(change) + " coins in Level: " + str(self.game.level_from_room(room).get_id()) + " Room: " + str(room.get_id()))
            print("miner loop end *****************************")
            print(i)
    
    async def loop_for_win(self):
        async with self.lock:
            while(self.game.check_win() == False):
                await self.enter_room(self.find_room())
                await self.drop_coins()

    async def loop_one(self):
        async with self.lock:
            await self.enter_room(self.find_room())
            await self.drop_coins()