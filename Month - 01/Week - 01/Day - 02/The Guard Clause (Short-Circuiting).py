'''
The Guard Clause (Short-Circuiting)
Goal: Create a variable user = None. 
Write an if statement that checks if user is not None AND if user 
has "admin" access.
Constraint: You must perform both checks in a single line. It must not 
crash when user is None.
The Mechanics: Python uses Short-Circuit Evaluation.
In the expression if A and B: If A is False, the interpreter never 
executes B.This acts as a "Guard," preventing the code from trying to 
access attributes of a NoneType object, which would cause an 
AttributeError.
'''

user = None

if user is not None and user.get("role") == "admin":
    print("Admin access granted")
else:
    print("Access denied")