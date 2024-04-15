from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level
import helper_functions as hf
import random
import threading

def TestClassFunctionality():
    # deprecated
    new_miner = Miner("m1", 10, None)
    new_gamer = Gamer("g1", 2, None)
    new_room = Room("r1", new_miner, new_gamer, 5)
    new_level = Level("level 1", [new_room], [new_miner], [new_gamer])
    new_level.set_name("frank")
    print(str(new_level))

def TestMinerFunctionality():
    g = hf.NewGame(2,2,1,1)
    miners = g.get_miners()
    m = miners[0]
    room = m.find_room()
    m.enter_room(room)
    m.drop_coins()
    print("\n" + str(room))
    print("\n" + str(m))
    print("\n" + str(g.get_occ_m()))
    room = m.find_room()
    m.enter_room(room)
    print("\n" + str(room))
    print("\n" + str(m))
    print("\n" + str(g.get_occ_m()))

def TestGamerFunctionality():
    g = hf.NewGame(2, 2, 1, 1)
    for room in g.get_rooms():
        room.set_coins(random.randint(20,50))
    gamer = g.get_gamers()[0]
    gamer.loop(10)

def ThreadingTest():
    g = hf.NewGame(2, 2, 1, 1)
    gamer = g.get_gamers()[0]
    m = g.get_miners()[0]
    # t1 = threading.Thread(target=m.loop(), args)
    t2 = threading.Thread(target, args)

    t1.join()
    t2.join()



TestGamerFunctionality()