'''
DEEP DIVE: 9.4 Micro-Challenge: The One-Time Trap
Goal: Create a generator g. Loop through it once. Try to loop through it
again. Deep Dive: Generators are Exhaustible. Once iterated, the "cursor"
is at the end. You cannot rewind a generator; you must re-instantiate it.
'''

def gen():
    yield 1
    yield 2
    yield 3
# Create generator object
g = gen()

print("First loop:")
for x in g:
    print(x)

print("\nSecond loop:")
for x in g:
    print(x)   # Nothing will be printed
