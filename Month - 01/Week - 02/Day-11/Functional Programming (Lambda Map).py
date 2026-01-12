'''
Functional Programming (Lambda Map)
DEEP DIVE: 11.1 Micro-Challenge: The Anonymous Function
Goal: Write a function add (x, y) using lambda. 
Deep Dive: lambda creates a function object on the heap but assigns it 
no name (unless you bind it to a variable). It is purely syntactic 
sugar for single-expression functions.
'''

add = lambda x, y: x + y
print(add(3, 5))
print(add(-3, 5))  
print(add(3, -5))  
