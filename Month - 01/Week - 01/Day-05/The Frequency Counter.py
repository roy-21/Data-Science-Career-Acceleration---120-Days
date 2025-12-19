"""
DEEP DIVE: Micro-Challenge: The Frequency Counter
Goal: Input a string "banana". Create a dictionary that counts the 
frequency of each letter (e.g., {'b':1, 'a':3, 'n':2}).
Constraint: Use a standard for loop and if/else logic.
The Mechanics: This demonstrates **Dynamic Key Insertion**. 
As you loop through 'b', 'a', 'n', Python calculates the hash for each char.
If the hash address is empty → Create Key, Value = 1.
If the hash address is occupied → Value += 1.
"""

text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
