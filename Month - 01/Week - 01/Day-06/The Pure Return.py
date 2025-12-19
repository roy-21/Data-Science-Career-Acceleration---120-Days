'''
DEEP DIVE: Micro-Challenge: The Pure Return
Goal: Write a function add (a, b) that prints the sum but returns nothing. 
Assign the result to a variable res add (5, 5). Print res.
Observation: It prints None.
The Mechanics: Every Python function returns something. If you do not 
explicitly write return value, Python implicitly executes return None at 
the end. Best Practice: Functions should calculate and return values. 
The calling code should decide whether to print them.
'''

def add(a, b):
    return a + b

res = add(5, 5)
print(res)


