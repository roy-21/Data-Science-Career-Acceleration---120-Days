'''
DEEP DIVE: 8.5 Micro-Challenge: The String Builder (O(N2))
Goal: Loop 10,000 times and add a character to a string using += "a". 
Deep Dive: Strings are Immutable. Every time you do, Python destroys the 
old string and creates a brand new larger one in a new memory address. 
Fix: Use "".join(list_of_chars).
'''

def build_string():
    chars = []
    for _ in range(10_000):
        chars.append("a")
    return "".join(chars)

print(len(build_string()))