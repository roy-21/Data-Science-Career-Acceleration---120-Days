'''
Day 9: Infinite Memory (Generators)
DEEP DIVE: 9.1 Micro-Challenge: The Basic Yield
Goal: Write a function gen() that yields 1, then 2, then 3. 
Loop through it. Deep Dive: Unlike return, yield pauses the function
and saves the Stack Frame (local variables) in RAM. The function is 
"frozen" until you call it again.
'''

def gen():
    yield 1
    yield 2
    yield 3

# Loop through the generator
for value in gen():
    print(value)