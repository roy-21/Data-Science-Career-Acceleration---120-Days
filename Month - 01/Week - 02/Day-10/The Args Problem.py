'''
DEEP DIVE: 10.3 Micro-Challenge: The Args Problem
Goal: Try to decorate a function that takes arguments add (a, b) 
with a wrapper that takes none. 
Deep Dive: It crashes. The inner wrapper function MUST 
accept *args and **kwargs to be compatible with any target 
function signature.
'''

def wrapper(func):
    def inner(*args, **kwargs):
        print("Logging...")
        result = func(*args, **kwargs)
        return result
    return inner


@wrapper
def add(a, b):
    return a + b


print(add(1, 2))
print(add(a=5, b=7))