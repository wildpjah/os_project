import asyncio

class Room:
    def __init__(self):
        self._miner_inside = None
        self._lock = asyncio.Lock()  # Each room has its own lock

    async def enter(self, miner):
        async with self._lock:
            # Wait until the room is empty before allowing a new miner to enter
            while self._miner_inside is not None:
                await asyncio.sleep(0.1)  # Adjust as needed
            self._miner_inside = miner
            print(f"{miner} entered {self}")

    async def leave(self, miner):
        async with self._lock:
            if self._miner_inside == miner:
                self._miner_inside = None
                print(f"{miner} left {self}")

    def get_lock(self):
        return self._lock

async def miner_task(miner, room):
    while True:
        async with room.get_lock():
            await room.enter(miner)
        # Perform long-running operations outside the lock
        await asyncio.sleep(1)  # Delay after entering the room
        async with room.get_lock():
            await room.leave(miner)
        # Perform long-running operations outside the lock
        await asyncio.sleep(1)  # Delay before the next iteration

class Miner:
    def __init__(self, id):
        self.id = id

async def main():
    room = Room()

    miners = [Miner(i) for i in range(1, 4)]

    miner_tasks = [miner_task(miner, room) for miner in miners]

    await asyncio.gather(*miner_tasks)

asyncio.run(main())