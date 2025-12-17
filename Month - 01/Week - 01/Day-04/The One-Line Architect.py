'''
DEEP DIVE: Micro-Challenge: The One-Line Architect
Goal: Create a list of numbers from 1 to 10. Generate a new list containing 
the Squares of only the Even numbers.
Constraint: Do this in exactly one line using List Comprehension.
The Mechanics: Code: [x**2 for x in nums if x % 2 == 0] List Comprehensions 
are not just syntactic sugar; they are faster than standard for loops. 
They are optimized at the C-level, avoiding the overhead of the Python 
interpreter constantly appending to a list.
'''

nums = list(range(1, 11))
squares = [x**2 for x in nums if x % 2 == 0]
print(squares)