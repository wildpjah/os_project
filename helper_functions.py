from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level

#these will be helpers for main
#this is just an example:
def LevelUp(gamer, levels):
    #levels should be the array of levels in order.
    if gamer.get_gold() > 20:
        old_level = None
        for i, level in levels:
            if gamer in level.get_gamers:
                old_level = level
                new_level = levels[i+1]
                break
        
        level.remove(gamer)
        new_level.add(gamer)
        return True
    else: return False

def GetRandomName():
    # TODO
    # Right now this does not actually do the random name thing we discussed
    return "Level"