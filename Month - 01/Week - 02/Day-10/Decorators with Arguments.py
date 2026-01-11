'''
DEEP DIVE: 10.10 Micro-Challenge: Decorators with Arguments
Goal: Create a decorator that accepts a setting: @repeat (times=3). 
Deep Dive: This requires Three Levels of Nested Functions. 
1. The Factory (accepts 'times'). 
2. The Decorator (accepts 'func'). 
3. The Wrapper (accepts 'args').
'''

from functools import wraps

def repeat(times=1):
    """Decorator factory: repeats function 'times' times"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


# Example usage
@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
