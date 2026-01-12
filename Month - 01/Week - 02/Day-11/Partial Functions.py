'''
11.9 Micro-Challenge: Partial Functions 
Goal: Create a function power (base, exp). Use functools.partial to 
create a new function square(x) that locks exp-2. 
Deep Dive: Partials "freeze" arguments. This is useful when you need to 
pass a function to a callback (like in Ul frameworks) that expects fewer 
arguments.
'''

from functools import partial

def power(base, exp):
    return base ** exp

# Freeze exp=2 → square(x)
square = partial(power, exp=2)

# Test
print(square(5))  # 25
print(square(10)) # 100
