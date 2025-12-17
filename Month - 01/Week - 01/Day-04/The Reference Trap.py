"""
DEEP DIVE: Micro-Challenge: The Reference Trap
Goal: Create a list a = [1, 2, 3]. Set b = a. 
Change the first item of b to 99. Print a.
Observation: a also changes to [99, 2, 3].
The Mechanics: Lists are **Mutable Objects**. When you write b = a, 
you are copying the Reference (Memory Address), 
not the data. Both a and b point to the exact same memory block. 
Fix: Use b = a.copy() or b = a[:] to force Python to allocate 
a new list in memory.
"""


"""
#using copy() method to create a new list

a = [1, 2, 3]
b = a. copy()

b[1]=99
print(a)
print(b)
"""

#using slicing to create a new list
a = [1,2,3,4]
b=a[:]

#reference trap 
b[2]=100
print(a)
print(b)