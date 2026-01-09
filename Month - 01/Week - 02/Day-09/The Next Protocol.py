'''
DEEP DIVE: 9.5 Micro-Challenge: The Next Protocol
Goal: Manually call next (gen) until it crashes. Deep Dive: When a 
generator runs out of items, it raises a Stoplteration exception. 
for loops catch this exception silently to stop looping.
'''
def gen():
    yield 1
    yield 2
    yield 3


g = gen()

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # StopIteration (crash)