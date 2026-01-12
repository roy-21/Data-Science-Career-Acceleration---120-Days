'''
11.6 Micro-Challenge: The Zip Lock 
Goal: Combine names" ["A", "B"] and ages [20, 30] into a dictionary. 
Deep Dive: dict(zip(names, ages)). zip creates an iterator of tuples. 
dict() consumes those tuples to build the hash map.
'''

names = ["A", "B"]
ages = [20, 30]

result = dict(zip(names, ages))

print(result)
