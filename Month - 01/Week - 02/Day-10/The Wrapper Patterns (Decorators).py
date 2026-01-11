'''
Day 10: The Wrapper Patterns (Decorators)
DEEP DIVE: 10.1 Micro-Challenge: The Manual Wrapper
Goal: Write a function wrapper (func) that runs code before/after func. 
Apply it man-ually: new_func = wrapper (old_func). 
Deep Dive: This demystifies the syntax. A decorator is simply a function
that takes a function and returns a function.
'''

def wrapper(func):
    # inner function (this is the actual wrapper)
    def inner():
        print("Before Call")
        func()                 # call the original function
        print("After Call")
    return inner               # return the new function


# Original function
def old_func():
    print("Inside original function")


# Manually apply wrapper
new_func = wrapper(old_func)

# Call the wrapped function
new_func()