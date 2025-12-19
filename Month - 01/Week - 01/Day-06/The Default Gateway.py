'''
DEEP DIVE: Micro-Challenge: The Default Gateway
Goal: Write a function connect (port 3306) that prints "Connecting to [port]".
Call it once with no arguments, and once with 5432.
The Mechanics: This uses "Default Arguments**. When Python defines the 
function, it stores 3306 in memory. If the caller provides no argument, 
Python grabs this stored default. This allows for flexible APIs where common 
settings are optional.
'''

def connect(port=3306):
    print(f"Connecting to {port}")

# Call without argument (uses default)
connect()

# Call with custom argument
connect(5432)
