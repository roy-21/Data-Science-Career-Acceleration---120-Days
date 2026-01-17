'''
Day 14: The Final Boss (Algorithmic Logic)

DEEP DIVE: 14.1 Capstone: Two Sum (O(N))
Goal: Find two numbers in a list that add up to Target. 
Deep Dive: Naive: Nested Loops (O(N2)). Pro: Use a Dictionary (Seen Map).
Calculate needed = target current. If needed is in map, you win.
'''

def two_sum(nums, target):
    seen = {}  # number : index

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return None
