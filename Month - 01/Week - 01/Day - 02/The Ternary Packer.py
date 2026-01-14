'''
The Ternary Packer
Goal: You have a variable score 85. Assign a variable status to "Pass" 
if score > 70 else "Fail".
Constraint: Do this in exactly one line of code.
The Mechanics: This is a Conditional Expression: status "Pass"
if score >
70 else "Fail" Unlike a standard if/else block which controls flow, 
this expression evaluates to a value that is immediately assigned to
the variable stack. It is atomic and atomic operations are often 
slightly faster.
'''

score = 85

if score > 70:
    status = "Pass"
else:
    status = "Fail"
print(status)
# Using Ternary Operator
status = "Pass" if score > 70 else "Fail"
print(status)
