'''
DEEP DIVE: 11.3 Micro-Challenge: The Filter 
Goal: Remove all negative numbers from a list using filter(). 
Deep Dive: filter (func, list) keeps items where func (item) returns 
Truthy. Passing None as the function automatically filters out Falsy 
values (0, "", None).
'''

numbers = [-5, -1, 0, 2, 4, -3, 7]

positive_numbers = list(filter(lambda x: x >= 0, numbers))

print(positive_numbers)
