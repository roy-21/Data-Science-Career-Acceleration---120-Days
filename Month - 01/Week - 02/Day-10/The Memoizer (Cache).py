'''
DEEP DIVE: 10.7 Micro-Challenge: The Memoizer (Cache)
Goal: Write a @cache decorator that stores results of expensive function
calls in a dictionary. 
Deep Dive: If func (5) is called, check the dict. If key 5 exists, 
return it instantly (O(1)). If not, run the function and save 
the result. This optimizes recursion (e.g., Fibonacci).
'''
from functools import wraps

def cache(func):
    memo = {}  # Created once (closure)

    @wraps(func)
    def wrapper(n):
        # Check cache first (O(1))
        if n in memo:
            return memo[n]

        # Run expensive computation
        result = func(n)

        # Store result in cache
        memo[n] = result
        return result

    return wrapper