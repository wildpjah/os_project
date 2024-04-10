from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level

#these will be helpers for main
#this is just an example:
def LevelUp(gamer):
    if gamer.get_gold() > 20:
        level = GetGamerLevel(gamer)
        new_level = GetLevelByRank(level.rank())
        new_level.add(gamer)
        level.remove(gamer)