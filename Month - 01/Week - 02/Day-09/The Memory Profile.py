'''
DEEP DIVE: 9.2 Micro-Challenge: The Memory Profile
Goal: Compare sys.getsizeof () of a List Comprehension vs a Generator 
Expression for 1 million numbers. Deep Dive: [x for x in range(1M)] 
consumes ~8MB RAM (stores all numbers). (x for x in range(1M)) 
consumes ~100 Bytes (stores only the logic).
'''

import sys

# 1 million numbers
N = 1_000_000

# List Comprehension
list_comp = [x for x in range(N)]

# Generator Expression
gen_exp = (x for x in range(N))

# Memory usage
print("Memory used by List Comprehension:")
print(sys.getsizeof(list_comp), "bytes")

print("\nMemory used by Generator Expression:")
print(sys.getsizeof(gen_exp), "bytes")
