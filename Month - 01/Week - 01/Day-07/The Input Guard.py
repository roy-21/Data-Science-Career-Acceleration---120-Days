'''
DEEP DIVE: Micro-Challenge: The Input Guard
Goal: Write a script that asks the user for their age. If they type 
text (e.g., "twenty"), print "Numbers only" instead of crashing.
Constraint: Use try/except ValueError.
The Mechanics: When int ("text") fails, Python raises a Signal. Normally, 
this signal bubbles up and kills the program. The try block creates 
a "Safety Net." If a specific signal (ValueError) hits the net, the 
interpreter jumps immediately to the except block, skipping any remaining 
code in the try section.
'''

try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Numbers only")
