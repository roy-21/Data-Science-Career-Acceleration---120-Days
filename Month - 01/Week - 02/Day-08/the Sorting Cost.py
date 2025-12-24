'''
DEEP DIVE: 8.8 Micro-Challenge: The Sorting Cost (O(N log N))
Goal: Sort a random list. 
Deep Dive: Python uses Timsort 
(a hybrid of Merge Sort and Insertion Sort). 
It is faster than O(N2) but slower than O(N). 
Avoid sorting inside loops!
'''

import random
def sort_random_list(size):
    random_list = [random.randint(0, size) for _ in range(size)]
    random_list.sort()
    return random_list

print(sort_random_list(100))

