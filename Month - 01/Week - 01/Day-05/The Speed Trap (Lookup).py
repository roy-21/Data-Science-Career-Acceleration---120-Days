"""
DEEP DIVE: Micro-Challenge: The Speed Trap (Lookup)
Goal: Create a list of 1 million numbers. Create a set (hash table) of the 
same numbers. Check if the number 1 exists in both.
Constraint: You don't need to actually run 1M items, but explain why the 
Set/Dict is faster.
The Mechanics:
List Search (O(N)): Python must scan item 1, item 2, item 3... until the 
end.
Dict/Set Search (0(1)): Python runs hash(-1), gets a memory address 
(e.g., 0x99), and looks only at that spot. It is instant.
"""

#create a list and set
numbers_list = list(range(1, 100001))
numbers_set = set(numbers_list)

#using sequential search
print(1 in numbers_list) #(O(N))
#using hash function
print(1 in numbers_set)  #(O(1))


"""
List lookup is linear time because it scans elements sequentially,
while set lookup is constant time due to hash-based indexing.
"""