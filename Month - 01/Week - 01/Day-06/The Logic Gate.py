'''
DEEP DIVE: Micro-Challenge: The Logic Gate
Goal: Write a function is_even (num) that returns True if even, 
False otherwise.
Constraint: Do not use if/else. Do it in one line.
The Mechanics: Code: return num %20 Comparison operators (like) 
evalu-ate directly to a Boolean value. You don't need to check if True return
True. You can simply return the result of the comparison itself.
'''

def is_even(num):
    return num % 2 == 0

num = 4
print(is_even(num))
num = 5
print(is_even(num))