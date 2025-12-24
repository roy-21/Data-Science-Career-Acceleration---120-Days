'''
DEEP DIVE: 8.9 Micro-Challenge: The Dictionary Creator (O(N))
Goal: Measure the time to create a dict from a list vs searching it. 
Deep Dive: Search-ing is O(1), but building the dictionary takes O(N) 
because Python must calculate the hash for every single item and 
allocate memory buckets.
'''

import time

def dict_creation_vs_search():
    data = list(range(1_000_000))

    # Measure dictionary creation time
    start = time.time()
    d = {x: True for x in data}
    creation_time = time.time() - start

    # Measure dictionary search time
    start = time.time()
    _ = 999_999 in d
    search_time = time.time() - start

    print("Dict creation time:", creation_time)
    print("Dict search time:", search_time)


dict_creation_vs_search()

