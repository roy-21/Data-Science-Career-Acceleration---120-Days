'''
DEEP DIVE: Micro-Challenge: The Stack Emulator
Goal: Create an empty list. Add numbers 1, 2, 3. Then remove the last 
number (3) and print it.
Constraint: Use.append() and pop(). Do not use insert() or remove().
The Mechanics: This mimics a LIFO (Last-In, First-Out) Stack.
append() and pop() are optimized to O(1) time complexity because Python 
lists are "Dynamic Arrays." Adding/removing from the end is instant.
.insert(0, x) is O(N) because Python must shift every other item in 
memory to make room.
'''

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

last_item = stack.pop()

print(last_item)