'''
DEEP DIVE: Micro-Challenge: The Truthiness Inspector
Goal: Create a variable data (Empty List). Write an if statement to 
print "Data Found" or "No Data" without comparing it to anything 
(e.g., do not use len(data) > 0).
The Mechanics: Python objects have inherent Boolean values.
Falsy: 0, 0.0, None, False, empty collections ("", [], {}).
Truthy: Everything else.
The interpreter implicitly calls bool (data) behind the scenes, making 
code cleaner and faster.
'''

data = []

if data:
    print("Data Found")
else:
    print("No Data")
