'''
11.4 Micro-Challenge: The Reducer
Goal: Calculate the product of a list (1*2*3*4) using functools.reduce. 
Deep Dive: Reduce collapses a list into a single value. 
It takes item 1 and 2, applies the function, takes the result and item 3,
applies again... until one item remains.
'''
from functools import reduce

numbers = [1, 2, 3, 4]

product = reduce(lambda x, y: x * y, numbers)

print(product)


