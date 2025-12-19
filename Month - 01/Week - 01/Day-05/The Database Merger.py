"""
DEEP DIVE: Micro-Challenge: The Database Merger
Goal: You have two dictionaries: 
defaults = { "theme": "light", "audio": "on"} and 
user_pref = { "theme": "dark"}. Merge them so user_pref overrides defaults.
Constraint: Use the update operator | (Python 3.9+) or update().
The Mechanics: When merging, Python iterates through the second dictionary. 
It cal-culates the hash of "theme". It finds that "theme" already exists 
in the first dictionary's memory block, so it **Overwrites** the value. 
It finds "audio" is missing in the second, so it keeps the original.  
"""

defaults = {"theme": "light", "audio": "on"}
user_pref = {"theme": "dark"}

merged = defaults.copy()
merged.update(user_pref)

print(merged)
