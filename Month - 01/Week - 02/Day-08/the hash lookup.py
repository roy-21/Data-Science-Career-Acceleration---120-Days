'''
DEEP DIVE: 8.2 Micro-Challenge: The Hash Lookup (0(1))
Goal: Convert that list to a set. Check for -5 again. Deep Dive: Python 
runs hash (-5), gets a memory address, and looks directly at that slot. 
It never scans the other items. Complexity: O(1). Constant time, 
regardless of data size.
'''
def hash_lookup():
    number = list(range(10000000))
    number_set = set(number)
    if -5 in number_set:
        return True
    else:
        return False

print(hash_lookup())

#Set uses hashing to directly access the memory location of an element.
