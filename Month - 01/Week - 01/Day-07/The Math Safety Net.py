'''
DEEP DIVE: Micro-Challenge: The Math Safety Net
Goal: create a variable x = 0. Try to print 100/x. Catch the specific error 
that occurs
The Mechanics: Division by zero is mathematically undefined. At the CPU level,
the ALU (Arithmetic Logic Unit) throws a hardware interrupt. Python wraps 
this into a ZeroDivisionError object. Catching this allows your data 
pipeline to say "Skipping bad row" instead of halting a 10-hour process.
'''
x = 0

try:
    result = 100 / x
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
