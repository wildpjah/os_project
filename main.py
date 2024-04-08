from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room

new_miner = Miner("m1", 10, True)
print(new_miner)
new_gamer = Gamer("g1", 2, True)
print(new_gamer)
new_room = Room("r1", new_miner, new_gamer, 5)
print(new_room)