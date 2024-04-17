from objects.Gamer import Gamer
from objects.Miner import Miner
from objects.Room import Room
from objects.Level import Level
import helper_functions as hf
import random
import threading
import concurrent.futures

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

    m_pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(g.get_miners() + g.get_gamers()))
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

    while g.check_win() == False:
        m_pool = concurrent.futures.ThreadPoolExecutor(max_workers=8)
        #gamer_pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(g.get_gamers()))
        m_pool.submit(miners[0].loop_one())
        m_pool.submit(gamers[0].loop_one())
        #g_pool.shutdown(wait=True)
        m_pool.shutdown(wait=True)


def ThreadingExample():
    URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistant-subdomain.python.org/']

    # Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))




ThreadingTest2()