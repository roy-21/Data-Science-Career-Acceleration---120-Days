'''
DEEP DIVE: 10.4 Micro-Challenge: The Return Value Thief
Goal: Write a decorator that forgets to return func(*args). 
Print the result of the decorated function. 
Deep Dive: It prints None. A wrapper must explicitly capture and return 
the result of the original function, otherwise the data is lost inside 
the wrapper scope.
'''

def working_wrapper(func):
    def inner(*args, **kwargs):
        print("Calling function...")
        value = func(*args, **kwargs)  #capture result
        return value                   #return result
    return inner


@working_wrapper
def add(a, b):
    return a + b


result = add(3, 4)
print(result)