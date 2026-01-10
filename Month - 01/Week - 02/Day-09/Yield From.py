'''
DEEP DIVE: 9.8 Micro-Challenge: Yield From
Goal: Write a generator that yields values from two different 
sub-generators using yield from. Deep Dive: yield from delegates 
the generator operation to another sub-generator. It flattens nested 
structures efficiently without manual loops.
'''

# Sub-generator 1
def gen_a():
    yield 1
    yield 2
    yield 3

# Sub-generator 2
def gen_b():
    yield 4
    yield 5
    yield 6

# Main generator using yield from
def main_gen():
    yield from gen_a()
    yield from gen_b()


# Consume the generator
for value in main_gen():
    print(value)
