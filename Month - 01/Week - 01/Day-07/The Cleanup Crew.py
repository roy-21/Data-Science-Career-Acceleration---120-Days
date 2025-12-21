'''
DEEP DIVE: Micro-Challenge: The Cleanup Crew
Goal: Write a try/except block that divides two numbers. Add a finally block 
that prints "Execution Complete" regardless of whether the division succeeded 
or failed.
The Mechanics: The finally block is guaranteed to run. Even if the program 
crashes or returns early in the try, Python ensures the finally code executes 
before leav-ing the scope. This is critical for "Resource Management" 
(closing files, database connections, or network sockets) to prevent 
memory leaks.
'''
a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Division failed: cannot divide by zero")
finally:
    print("Execution Complete")
