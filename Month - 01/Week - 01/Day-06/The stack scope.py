'''
DEEP DIVE: Theory: The Stack Scope
When a function is called, Python creates a "Stack Frame" in memory. 
All variables created inside the function live there. When the function 
returns, the frame is destroyed. 
LEGB Rule: Python searches for variables in this order: 
Local -> Enclosing -> Global -> Built-in.
'''

def calculate_area (radius: float) -> float:
# """Returns area of circle. Inputs float."""
    if radius < 0:
        return 0
    return 3.14 * (radius**2)

# Main Execution
r = 5
print(calculate_area(r))