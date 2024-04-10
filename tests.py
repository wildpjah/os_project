from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level

def TestClassFunctionality():
    new_miner = Miner("m1", 10, None)
    new_gamer = Gamer("g1", 2, None)
    new_room = Room("r1", new_miner, new_gamer, 5)
    new_level = Level("level 1", [new_room], [new_miner], [new_gamer])
    new_level.set_name("frank")
    print(str(new_level))

TestClassFunctionality()