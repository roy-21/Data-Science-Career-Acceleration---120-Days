'''
11.7 Micro-Challenge: List Comprehension Speed
Goal: Compare map (lambda...) vs [x... for x...]. 
Deep Dive: List Comprehen-sions are generally faster 
than map + lambda because they avoid the overhead of calling a Python 
function frame for every single item.
'''

data = [1, 2, 3, 4, 5]

# map + lambda
map_result = list(map(lambda x: x * x, data))

# list comprehension
lc_result = [x * x for x in data]

print(map_result)
print(lc_result)
