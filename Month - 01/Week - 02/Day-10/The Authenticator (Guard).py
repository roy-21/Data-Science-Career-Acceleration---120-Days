'''
DEEP DIVE: 10.6 Micro-Challenge: The Authenticator (Guard) 
Goal: Create @admin_required. If global USER != 'admin', raise 
PermissionError. 
Deep Dive: The decorator acts as a gatekeeper. It executes before the 
sensitive function is entered. If the check fails, the stack frame for 
the target function is never even created.
'''
from functools import wraps

def memoize(func):
    cache = {}  # lives in enclosing scope (closure)

    @wraps(func)
    def wrapper(n):
        if n in cache:
            return cache[n]   # O(1) lookup
        value = func(n)       # expensive calculation
        cache[n] = value      # store result
        return value

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Test
print(fibonacci(10))
print(fibonacci(10))  # cached, instant
