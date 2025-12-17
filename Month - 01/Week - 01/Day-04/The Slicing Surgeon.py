"""
DEEP DIVE: Micro-Challenge: The Slicing Surgeon
Goal: Create a list data = [10, 20, 30, 40, 50]. Create a new list containing
the last 3 items in reverse order.
Constraint: Use Slicing syntax [start:stop:step].
The Mechanics: The syntax data [-1:-4:-1] or data[:1:-1] creates a 
**Shallow Copy**. Unlike simple assignment, slicing tells the 
interpreter: "Go to this memory block, read these specific values, 
and build a New Object to hold them." This leaves the original list 
untouched.
"""

data = [10, 20, 30, 40, 50]

result = data[-1:-4:-1]

print(result)