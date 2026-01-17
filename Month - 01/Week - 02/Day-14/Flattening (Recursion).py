'''
DEEP DIVE: 14.4 Capstone: Flattening (Recursion)
Goal: Flatten [1, [2, [3, 4]]] into [1, 2, 3, 4]. 
Deep Dive: Write a recursive function. If item is list recurse. 
Else yield.
'''

def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result
