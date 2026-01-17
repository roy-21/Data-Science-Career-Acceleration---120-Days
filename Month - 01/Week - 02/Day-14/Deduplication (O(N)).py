'''
DEEP DIVE: 14.6 Capstone: Deduplication (O(N))
Goal: Remove duplicates from a list while keeping order. 
Deep Dive: list (set(x)) destroys order. Solution: Iterate, check if 
item in seen set, if not append to result.
'''

def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
