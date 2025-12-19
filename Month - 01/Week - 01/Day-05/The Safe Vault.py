"""
DEEP DIVE: Micro-Challenge: The Safe Vault
Goal: Create a dictionary user = {"id": 1}. Try to access user ["email"]. 
Then try to access it safely.
Constraint: Use.get().
The Mechanics: Direct access user ["key"] raises a KeyError if the key is 
missing, crashing the script. The method user.get("key", "Default") checks 
the Hash Table. If the bucket is empty, it returns your default value 
(or None) instead of raising an error signal.
"""


user = {"id": 1}

email = user.get("email", "Email not found")
print(email)