'''
DEEP DIVE: 8.6 Micro-Challenge: The Length Trick (0(1))
Goal: Call len() on a list of 1 billion items. 
Deep Dive: You might expect Python to count items one by one. 
It doesn't. The C-structure of a Python list maintains a metadata 
counter ob_size. len() simply reads this cached integer. 
It is instant.
'''
def length():
    numbers = list(range(10_000_000))
    return len(numbers)

print(length())