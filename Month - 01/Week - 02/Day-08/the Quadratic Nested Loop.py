'''
DEEP DIVE: 8.7 Micro-Challenge: The Quadratic Nested Loop (O(N2))
Goal: Find duplicates between two lists using nested for loops. 
Deep Dive: For every item in List A, you scan all items in 
List B. 10,000 × 10,000 = 100,000,000 operations.
This is the most common cause of server timeouts.
'''

def find_duplicates(list_a, list_b):
    matches = []
    for iteam_a in list_a:
        for item_b in list_b:
            if iteam_a == item_b:
                matches.append(iteam_a)
                
    return matches

list_a = list(range(10_000))
list_b = list(range(5_000, 15_000))

print(len(find_duplicates(list_a, list_b)))