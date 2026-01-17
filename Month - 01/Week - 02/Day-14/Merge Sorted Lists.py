'''
DEEP DIVE: 14.10 Capstone: Merge Sorted Lists
Goal: Combine two sorted lists into one sorted list (O(N)). 
Deep Dive: Two Pointers. Compare head of A and head of B. Take smaller. 
Move pointer. Repeat.
'''

def merge_sorted_lists(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # add remaining elements
    result.extend(a[i:])
    result.extend(b[j:])

    return result
