'''
11.8 Micro-Challenge: Any All
Goal: Check if any number in a list is negative. Check if all are 
positive. 
Deep Dive: These are short-circuiting operators. any() stops at the
first True. all() stops at the first False. This is O(1) in the best 
case.
'''

numbers = [-3, 5, 8, 10]

has_negative = any(x < 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)

print(has_negative)
print(all_positive)
