'''
DEEP DIVE: 10.5 Micro-Challenge: The Timer (Performance)
Goal: Create a @timer decorator that prints execution time using time.
time(). 
Deep Dive: This is AOP (Aspect Oriented Programming). We inject timing 
logic into the function without modifying the function's actual code.
'''

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()          # start clock
        result = func(*args, **kwargs)    # run business logic
        end_time = time.time()            # end clock
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        return result                     # return original result
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    return "Task Completed"


# Call the decorated function
output = slow_function()
print(output)
