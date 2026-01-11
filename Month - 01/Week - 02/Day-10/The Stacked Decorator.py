'''
DEEP DIVE: 10.9 Micro-Challenge: The Stacked Decorator
Goal: Apply two decorators: @bold and @italic to a string returning 
function. 
Deep Dive: Decorators stack from bottom to top (Inner to Outer). 
@bold @italic becomes bold(italic (func())). Order matters!
'''

from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def italic(func):
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper


@bold
@italic
def greet():
    return "Hello World"


print(greet())
