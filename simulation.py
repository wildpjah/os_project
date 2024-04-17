import threading
import random
import time

# Define constants
GAMERS_COUNT = 10
MINERS_COUNT = 20
LEVELS_COUNT = 10
ROOMS_PER_LEVEL = 3
SEARCH_TIME_BASE = 10  # milliseconds
MINER_STAY_TIME = 0.00001  # seconds (10 nanoseconds)
GOLD_TO_COLLECT = 20

# Define global variables
levels = [[] for _ in range(LEVELS_COUNT)]
gamer_queue = list(range(GAMERS_COUNT))
gold_collected = [0] * GAMERS_COUNT
level_search_time = [SEARCH_TIME_BASE - i for i in range(LEVELS_COUNT)]


def miner_behavior(miner_id):
    time.sleep(0.1)  # Miners get 100 milliseconds to start
    while True:
        room_level = random.randint(0, LEVELS_COUNT - 1)
        room_number = random.randint(0, ROOMS_PER_LEVEL - 1)
        print(f"Miner{miner_id} dropped {random.randint(1, 5)} gold coins in room {room_level * ROOMS_PER_LEVEL + room_number}")
        time.sleep(MINER_STAY_TIME)


def gamer_behavior(gamer_id):
    while gold_collected[gamer_id] < GOLD_TO_COLLECT:
        current_level = gold_collected[gamer_id] // ROOMS_PER_LEVEL
        if len(levels[current_level]) == 0:
            # Wait until a room is available in the current level
            time.sleep(0.1)
            continue
        # Choose a room at random from the current level
        room_number = random.choice(levels[current_level])
        print(f"Gamer{gamer_id} collected 1 gold coin in room {current_level * ROOMS_PER_LEVEL + room_number}")
        gold_collected[gamer_id] += 1
        time.sleep(level_search_time[current_level] / 1000)  # Convert milliseconds to seconds
    print(f"Gamer{gamer_id} has collected 20 gold coins and moved to the next level")


def main():
    # Create miner threads
    miner_threads = []
    for i in range(MINERS_COUNT):
        t = threading.Thread(target=miner_behavior, args=(i,))
        miner_threads.append(t)
        t.start()

    # Create gamer threads
    gamer_threads = []
    for i in range(GAMERS_COUNT):
        t = threading.Thread(target=gamer_behavior, args=(i,))
        gamer_threads.append(t)
        t.start()

    # Join threads
    for t in miner_threads:
        t.join()
    for t in gamer_threads:
        t.join()


if __name__ == "__main__":
    main()
