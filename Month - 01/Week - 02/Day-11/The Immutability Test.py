'''
11.10 Micro-Challenge: The Immutability Test
Goal: Try to modify a tuple inside a map function. 
Deep Dive: Functional programming relies on "Immutability. 
Functions should not have side effects (modifying global state). 
They should receive input and return new output.
'''
numbers = [(1, 2), (3, 4), (5, 6)]

# Pure function that returns new tuple
def add_one_to_tuple(t):
    return (t[0] + 1, t[1] + 1)

# map applies function to every tuple, original untouched
new_numbers = list(map(add_one_to_tuple, numbers))

print("Original:", numbers)
print("New:", new_numbers)
