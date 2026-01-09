'''
DEEP DIVE: 9.10 Micro-Challenge: State Retention
Goal: Write a generator that calculates a "Running Average". 
Deep Dive: The gen-erator remembers the total and count variables 
between yields. This eliminates the need for global variables or 
class attributes.
'''

def running_average():
    total = 0
    count = 0
    avg = None
    while True:
        num = yield avg  # pause & wait for new input
        if num is None:
            continue  # skip if no number sent
        total += num
        count += 1
        avg = total / count


# Create generator object
ra = running_average()

# Start the generator (must call next first)
print(next(ra))  

# Send numbers one by one
print(ra.send(10))  
print(ra.send(20))  
print(ra.send(30))  
print(ra.send(40))  