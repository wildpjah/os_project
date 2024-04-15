from objects.Game import Game
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

def NewGame(num_levels, num_rooms, num_gamers, num_miners):
    g = Game("Bruh")
    # initialize amounts
    num_levels = num_levels
    # number of rooms is per level
    num_rooms = num_rooms
    num_gamers = num_gamers
    num_miners = num_miners
    # levels holds all levels in order of progression. order of other lists does not matter.
    levels = []
    rooms = []
    gamers = []
    miners = []
    #list of occupied and unoccupied rooms
    occ_m = []
    occ_g = []
    un_occ_m = []
    un_occ_g = []

    # initialize Levels and Rooms
    for i in range(1, num_levels + 1):
        # create a new level and append it to the array
        new_level = Level(g, i, GetRandomName(), [], [], [])
        levels.append(new_level)
        # initialize Rooms and put them in our level too
        for i in range(1, num_rooms + 1):
            new_room = Room(g, i, "Room", None, None, 0)
            new_level.add_room(new_room)
            rooms.append(new_room)
            un_occ_m.append(new_room)
            un_occ_g.append(new_room)
    # initialize Gamers in level 1
    for i in range(1, num_gamers + 1):
        new_gamer = Gamer(g, i, "Gamer")
        gamers.append(new_gamer)
        levels[0].add_gamer(new_gamer)
    
    # initialize Miners
    for i in range(1, num_miners + 1):
        miners.append(Miner(g, i, "Miner"))
    g.set_levels(levels)
    g.set_rooms(rooms)
    g.set_gamers(gamers)
    g.set_miners(miners)
    g.set_occ_m(occ_m)
    g.set_un_occ_m(un_occ_m)
    g.set_occ_g(occ_g)
    g.set_un_occ_g(un_occ_g)
    return g
                
                

    def DeclareVictory(gamer):
        print(str(gamer) + "\nFIRST PLACE VICTORY")
        print("******************************")