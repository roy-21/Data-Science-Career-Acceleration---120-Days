'''
DEEP DIVE: Micro-Challenge: The Custom Signal
Goal: Ask the user for a number. If the number is negative, manually trigger 
an error using raise ValueError("No negatives").
The Mechanics: You can enforce your own logic rules by "raising" exceptions 
manually. When you write raise, you are constructing an Exception Object and 
handing it to the Python interpreter, forcing it to stop normal execution and 
look for an exception handier (just like a built-in error).
'''

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise ValueError("No negatives")
    
    print(f"You entered: {num}")

except ValueError as e:
    print(e)