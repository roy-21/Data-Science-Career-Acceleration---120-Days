'''
DEEP DIVE: 8.3 Micro-Challenge: The Insertion Trap (Ο(Ν))
Goal: Compare list.append(x) VS list.insert(0, x). Deep Dive: append() 
puts data in the next empty memory slot (O(1)).. insert(0, x) forces 
Python to shift every single existing item one step to the right in 
memory to make room. Result: Inserting at the start of a large list 
is catastrophic for performance.
'''
import time

def append_vs_insert():
    numbers = list(range(1_000_000))

    # append() test
    start = time.time()
    numbers.append(-1)
    append_time = time.time() - start

    # insert(0, x) test
    start = time.time()
    numbers.insert(0, -2)
    insert_time = time.time() - start

    print("Append time:", append_time)
    print("Insert(0, x) time:", insert_time)


append_vs_insert()
