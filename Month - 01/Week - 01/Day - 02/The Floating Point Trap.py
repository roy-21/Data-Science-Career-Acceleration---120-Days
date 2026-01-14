'''
DEEP DIVE: Micro-Challenge: The Floating Point Trap
Goal: Write a script that checks if 0.1 + 0.2 == 0.3. 
Print the result (True/False).
Observation: It prints False.
The Mechanics: Computers use binary (Base-2) to store numbers. 
Just as 1/3 cannot be represented perfectly in decimal (0.333...), 0.1 
cannot be represented perfectly in binary. The actual sum in memory 
is 0.30000000000000004. Fix: Always use a tolerance threshold (epsilon)
or round() when comparing floats in Data Science.
'''

epsilon = 1e-9

result = abs((0.1 + 0.2) - 0.3) < epsilon
print(result)
