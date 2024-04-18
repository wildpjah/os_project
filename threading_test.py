import threading
import concurrent.futures
import urllib.request
import asyncio


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


print("program continues\n******************")
class MyClass:
    def method1(self):
        i=0
        while(i<20):
            print("m1")
            i = i + 1
        pass

    def method2(self):
        i=0
        while(i<20):
            print("mmmmmmmmmmmmmmmmmm2")
            i = i + 1
        pass

# Create instances of MyClass
obj1 = MyClass()
obj2 = MyClass()

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit method1 from obj1
    future1 = executor.submit(obj1.method1)

    # Submit method2 from obj2
    future2 = executor.submit(obj2.method2)

print("program continues\n******************")




async def method1():
    for i in range(20):
        print("m1")
        await asyncio.sleep(0.1)

async def method2():
    for i in range(20):
        print("mmmmmmmmm2")
        await asyncio.sleep(0.1)

async def main():
    await asyncio.gather(method1(), method2())

asyncio.run(main())
print("program continues\n******************")


import asyncio

class MyClass:
    async def my_method(self, instance_id):
        for i in range(5):
            print(f"Method execution for instance {instance_id}, iteration {i}")
            await asyncio.sleep(0.1)

async def main():
    instances = [MyClass() for _ in range(3)]  # Create multiple instances of MyClass
    coroutines = [instance.my_method(instance_id) for instance_id, instance in enumerate(instances)]
    await asyncio.gather(*coroutines)

asyncio.run(main())