import threading
import concurrent.futures
import urllib.request


bruh = False

def opp1(t):
    global bruh
    i=0
    while(bruh == False and i<t):
        print("m")
        i = i + 1
    bruh = True
    print("finished, bruh = " + str(bruh) + "i=" + str(i))

def opp2(t):
    global bruh
    i=0
    while(bruh == False and i<t):
        print("gamer")
        i = i + 1
    bruh = True
    print("finished, bruh = " + str(bruh) + "i=" + str(i))


t1 = threading.Thread(target=opp1, args=(10,))
t2 = threading.Thread(target=opp2, args=(10,))
t1.start()
t2.start()

t1.join()
t2.join()
print("program continues\n******************")
bruh = False


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

print("program continues\n******************")
bruh = False
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Start the load operations and mark each future with its URL
    #my_future = {executor.submit(load_url, url, 60): url for url in URLS}
    f1 = executor.submit(opp1, 10)
    f2 = executor.submit(opp2, 10)
    futures = [f1, f2]
    for future in concurrent.futures.as_completed(futures):
        # url = future_to_url[future]
        # try:
        #     data = future.result()
        # except Exception as exc:
        #     print('%r generated an exception: %s' % (url, exc))
        # else:
        #     print('%r page is %d bytes' % (url, len(data)))
        print(str(future) + " is completed")

