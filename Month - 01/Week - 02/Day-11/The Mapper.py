'''
DEEP DIVE: 11.2 Micro-Challenge: The Mapper
Goal: Square a list of numbers using map (). 
Deep Dive: map (func, list) pushes the loop into C-speed. It returns an 
iterator (lazy), not a list. You must cast it with list() to trigger 
execution.
'''

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x * x, numbers))

print(squared_numbers)
