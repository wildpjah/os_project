from objects.Game import Game
from objects.Person import Person
from objects.Miner import Miner
from objects.Gamer import Gamer
from objects.Level import Level
from objects.Room import Room
import helper_functions as hf
import threading
import asyncio
import random


def main2():
    #generated code
    gamers = [Gamer(i) for i in range(1, 11)]  # Create 10 gamers
    miners = [Miner() for _ in range(20)]  # Create 20 miners
    levels = 10
    rooms_per_level = 3
    rooms = [[Room() for _ in range(rooms_per_level)] for _ in range(levels)]

    # Simulation loop
    while True:
        # Randomly choose a gamer
        current_gamer = random.choice(gamers)
        
        # Check if the gamer can progress to the next level
        if current_gamer.coins_collected >= 20:
            if current_gamer.level < levels:
                current_gamer.level += 1
                current_gamer.search_time -= 1  # Decrease search time by 1 ms

        # Randomly choose a room for the gamer to enter
        available_rooms = [room for room in rooms[current_gamer.level - 1] if room.gamer is None]
        if available_rooms:
            selected_room = random.choice(available_rooms)
            current_gamer.enter_room(selected_room)
            selected_room.gamer = current_gamer

            # Simulate gamer searching for gold coins
            time.sleep(current_gamer.search_time / 1000)  # Convert search time from ms to seconds

            # Gamer collects coins
            selected_room.coins += 1
            current_gamer.coins_collected += 1

            print(f"Gamer {current_gamer.id} collected 1 coin in room {rooms[current_gamer.level - 1].index(selected_room) + 1}")

            # Check if gamer collected enough coins to progress
            if current_gamer.coins_collected >= 20:
                print(f"Gamer {current_gamer.id} collected 20 coins and progressed to level {current_gamer.level}")

            selected_room.gamer.leave_room()
            selected_room.gamer = None


async def main():
    #initialize game
    random.seed()
    mg, g = hf.NewGame(10,3,10,20)

    gamers = g.get_gamers()
    miners = g.get_miners()
    tasks = []
    observer = Observer(mg)

    # Register the observer with the Game instance
    g.register_observer(observer)


    g.get_rooms()[3].add_coins(6)
    await miners[1].enter_room(g.get_rooms()[3])
    mg.data = g
    pygame_process = multiprocessing.Process(target=hf.AnimateGame, args=(mg,))
    pygame_process.start()
    
    
    for miner in miners:
        tasks.append(asyncio.create_task(miner.loop_for_t(50000000000)))
    for gamer in gamers:
        tasks.append(asyncio.create_task(gamer.loop_for_t(5000000000)))

    random.shuffle(tasks)
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print("Game Complete")
    pygame_process.join()

if __name__ == "__main__":
    asyncio.run(main())