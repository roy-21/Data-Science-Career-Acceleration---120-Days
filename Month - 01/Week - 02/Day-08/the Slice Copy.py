'''
DEEP DIVE: 8.10 Micro-Challenge: The Slice Copy (O(k))
Goal: Slice a massive list data [0:5000]. 
Deep Dive: Slicing is not free. It allocates new memory and copies the 
data references. Slicing a huge chunk takes time propor-tional to the 
slice size ().
'''
import time

def slice_cost():
    data = list(range(1_000_000))

    start = time.time()
    part = data[0:5000]
    print("Slice time:", time.time() - start)

    return part


print(len(slice_cost()))

