'''
DEEP DIVE: 9.9 Micro-Challenge: The Send Method
Goal: Use gen.send(value) to inject data into a running generator. 
Deep Dive: Gen-erators can be two-way streets. val yield pauses and 
waits to receive data from the outside world. This is the basis for 
Coroutines (AsyncIO).
'''

def gen():
    print("Generator started")
    val = yield "Initial yield"
    print("Received:", val)
    val2 = yield "Second yield"
    print("Received:", val2)


# Create generator object
g = gen()

# Start generator (must call next() first)
print(next(g))  # Output: Initial yield

# Send value into generator
print(g.send(100))  # Output: Second yield, prints Received: 100

# Send another value (generator may end)
try:
    g.send(200)
except StopIteration:
    print("Generator exhausted")