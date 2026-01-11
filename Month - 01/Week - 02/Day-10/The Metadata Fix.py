'''
DEEP DIVE: 10.8 Micro-Challenge: The Metadata Fix
Goal: Print func.__name__ of a decorated function. 
Deep Dive: It prints "wrapper", not the original name! 
This confuses debuggers. Fix: Use @functools.wraps (func) on the wrapper
to copy the original metadata (name, docstring) to the new function.
'''
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(a, b):
    """Adds two numbers"""
    return a + b


print(add.__name__)
print(add.__doc__) 
