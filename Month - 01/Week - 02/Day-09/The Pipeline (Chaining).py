'''
DEEP DIVE: 9.6 Micro-Challenge: The Pipeline (Chaining)
Goal: Create two generators: one squares numbers, the other filters 
evens. Chain them: filter (square (nums)). Deep Dive: This creates a 
Data Pipeline. Data flows from source → square 
filter one item at a time. No intermediate lists are created in RAM.
'''
# Number generator
def nums(n):
    for i in range(n):
        yield i

# Square generator
def square(source):
    for x in source:
        yield x * x

# Filter even generator
def filter_even(source):
    for x in source:
        if x % 2 == 0:
            yield x


# Chaining generators (Pipeline)
pipeline = filter_even(square(nums(10)))

# Consume the pipeline
for value in pipeline:
    print(value)