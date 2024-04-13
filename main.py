from objects.Person import Person
from objects.Miner import Miner
from objects.Gamer import Gamer
from objects.Room import Room
from objects.Level import Level
import helper_functions as hf


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


def main():
    # initialize amounts
    num_levels = 10
    # number of rooms is per level
    num_rooms = 3
    num_gamers = 10
    num_miners = 20
    # levels holds all levels in order of progression. order of other lists does not matter.
    levels = []
    rooms = []
    gamers = []
    miners = []

    # initialize Levels and Rooms
    for i in range(1, num_levels + 1):
        # create a new level and append it to the array
        new_level = Level(i, hf.GetRandomName())
        levels.append(new_level)
        # initialize Rooms and put them in our level too
        for i in range(1, num_rooms + 1):
            new_level.add_room(Room(i, "Room"))
    
    # initialize Gamers in level 1
    for i in range(1, num_gamers + 1):
        new_gamer = Gamer(i, "Gamer")
        gamers.append(new_gamer)
        levels[0].add_gamer(new_gamer)
    
    # initialize Miners
    for i in range(1, num_miners + 1):
        miners.append(Miner(i, "Miner"))
    print(levels[0])
    # run gamers in parallel and miners in parallel

    #for t in range(1, 1000):






if __name__ == "__main__":
    main()
