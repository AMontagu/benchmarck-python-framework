"""
Results on PC CPU i5 2520m (~ 10 year old), Windows, Python 3.8:

single char: ~ 350 requests/second 
db search: idem
"""

import requests, time, threading

NUM_REQUESTS = 1000
NUM_WORKERS = 10

threads = []

r = requests.get('http://127.0.0.1:5000/dbinsert')

start = time.time()

def req():
    for i in range(NUM_REQUESTS // NUM_WORKERS):
        # r = requests.get('http://127.0.0.1:5000/dbsearch')
        r = requests.get('http://127.0.0.1:5000/char')

for i in range(NUM_WORKERS):
    t = threading.Thread(target=req)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

elapsed_time = time.time() - start

print(NUM_REQUESTS / elapsed_time)
