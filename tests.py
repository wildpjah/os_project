from objects.Game import Game
from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level
import helper_functions as hf
import random
import threading
import concurrent.futures
import multiprocessing
import asyncio
import sys






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
    m.loop_for_t(10)

def TestGamerFunctionality():
    g = hf.NewGame(2, 2, 1, 1)
    for room in g.get_rooms():
        room.set_coins(random.randint(20,50))
    gamer = g.get_gamers()[0]
    gamer.loop_for_t(10)

def ThreadingTest():
    g = hf.NewGame(2, 2, 1, 1)
    gamer = g.get_gamers()[0]
    miners = g.get_miners()

    m_pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(g.get_miners() + g.get_gamers() + 1))
    #gamer_pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(g.get_gamers()))
    for miner in miners:
        m_pool.submit(miner.loop_for_win())
    for gamer in gamers:
        m_pool.submit(gamer.loop_for_win())
    #g_pool.shutdown(wait=True)
    m_pool.shutdown(wait=True)

    # t1 = threading.Thread(target=m.loop_for_win())
    # t2 = threading.Thread(target=gamer.loop_for_win())

    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

def ThreadingTest2():
    g = hf.NewGame(2, 2, 1, 1)
    gamers = g.get_gamers()
    miners = g.get_miners()

    m_pool = concurrent.futures.ProcessPoolExecutor(max_workers=16)
    #gamer_pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(g.get_gamers()))
    m_pool.submit(miners[0].loop_for_t(200))
    m_pool.submit(gamers[0].loop_for_t(200))
    #g_pool.shutdown(wait=True)
    m_pool.shutdown(wait=True)

def ThreadingTest3():
    g = hf.NewGame(2, 2, 1, 1)
    gamers = g.get_gamers()
    miners = g.get_miners()

    t1 = multiprocessing.Process(target=miners[0].loop_for_t(200), name="miners")
    t2 = multiprocessing.Process(target=gamers[0].loop_for_t(200), name="gamers")

    t2.start()
    t1.start()
    t2.join()
    t1.join()

def ThreadingTest4():
    g = hf.NewGame(2, 2, 1, 1)
    gamers = g.get_gamers()
    miners = g.get_miners()

    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as pool:
        pool.submit(miners[0].loop_for_t(200))
        pool.submit(gamers[0].loop_for_t(200))

async def ThreadingTest5():
    g = hf.NewGame(2, 2, 1, 1)
    gamers = g.get_gamers()
    miners = g.get_miners()

    miner_task = miners[0].loop_for_t(200)
    gamer_task = gamers[0].loop_for_t(200)

    await asyncio.gather(miner_task, gamer_task)

async def ThreadingTest6():
    g = hf.NewGame(2, 2, 2, 2)
    gamers = g.get_gamers()
    miners = g.get_miners()
    m_tasks = []
    g_tasks = []

    # Start concurrent execution of miner and gamer tasks
    for miner in miners:
        m_tasks.append(miner.loop_for_t(200))
    for gamer in gamers:
        g_tasks.append(gamer.loop_for_t(200))

    # Wait for all tasks to complete
    await asyncio.gather(*m_tasks, *g_tasks)


async def ThreadingTest7():
    g = hf.NewGame(10,3,10,20)
    gamers = g.get_gamers()
    miners = g.get_miners()
    tasks = []

    # Create tasks for miners and gamers
    for miner in miners:
        tasks.append(asyncio.create_task(miner.loop_for_t(500)))
    for gamer in gamers:
        tasks.append(asyncio.create_task(gamer.loop_for_t(500)))

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

async def ThreadingTest8():
    #This is essentially the same as test 6, but I want to remove the complication of multiple rooms and levels to focus on deadlocks for 1 room only
    g = hf.NewGame(1, 1, 2, 2)
    gamers = g.get_gamers()
    miners = g.get_miners()
    m_tasks = []
    g_tasks = []

    # Start concurrent execution of miner and gamer tasks
    for miner in miners:
        m_tasks.append(miner.loop_for_t(200))
    for gamer in gamers:
        g_tasks.append(gamer.loop_for_t(200))

    # Wait for all tasks to complete
    await asyncio.gather(*m_tasks, *g_tasks)

async def ThreadingTest9():
    random.seed()
    g = hf.NewGame(10,3,10,20)
    gamers = g.get_gamers()
    miners = g.get_miners()
    tasks = []

    # Create tasks for miners and gamers
    for miner in miners:
        tasks.append(asyncio.create_task(miner.loop_for_win()))
    for gamer in gamers:
        tasks.append(asyncio.create_task(gamer.loop_for_win()))

    random.shuffle(tasks)
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print("Game Complete")

async def AnimationTest1():
    #initialize game
    random.seed()
    g = hf.NewGame(10,3,10,20)

    gamers = g.get_gamers()
    miners = g.get_miners()
    tasks = []
    g.get_rooms()[3].add_coins(6)

    pygame_process = multiprocessing.Process(target=hf.AnimateGame, args=(g,))
    pygame_process.start()
    pygame_process.join()
    g.get_rooms()[4].add_coins(6)
    
    for miner in miners:
        tasks.append(asyncio.create_task(miner.loop_for_t(500)))
    for gamer in gamers:
        tasks.append(asyncio.create_task(gamer.loop_for_t(500)))

    random.shuffle(tasks)
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    print("Game Complete")

    # # Initialize Pygame
    # pygame.init()

    # # Set up the display
    # screen = pygame.display.set_mode((800, 600))
    # pygame.display.set_caption("Pygame Drawing Example")


# Threading Testing!
# There's too much text to fit in a terminal so I will put it in a file
# Save the current stdout so that we can revert sys.stdou after we complete
# our redirection

# stdout_fileno = sys.stdout
# sys.stdout = open('output.txt', 'w')

# asyncio.run(ThreadingTest9())

# sys.stdout.close()
# sys.stdout = stdout_fileno


# Animation Testing!

asyncio.run(AnimationTest1())