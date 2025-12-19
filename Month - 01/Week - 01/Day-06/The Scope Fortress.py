'''
DEEP DIVE: Micro-Challenge: The Scope Fortress
Goal: Create a global variable x = 10. Write a function change_x() that 
sets x = 20 inside it. Print x outside the function.
Observation: It prints 10, not 20.
The Mechanics: This demonstrates **Local vs. Global Scope**. 
When you write x = 20 inside a function, Python creates a new local variable 
named 'x' inside the function's stack frame. It does NOT touch the 
global 'x'. To modify the global, you would need the global 
keyword (but avoid this in production!).
'''
# #case1-- without global keyword
# x = 10

# def change_x():
#     x = 20  # local variable
#     print("Inside function:", x)

# change_x()
# print("Outside function:", x)

#-------------------------------------------------
#use global keyword 
x = 10

def change_x():
    global x
    x = 20
change_x()
print(x)



