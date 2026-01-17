'''
DEEP DIVE: 14.2 Capstone: The Palindrome (Slicing)
Goal: Check if a string is a palindrome (ignoring space/case). 
Deep Dive: Clean string ss[::-1]. Slicing creates a reversed copy in 
memory.
'''

def is_palindrome(s):
    # clean the string: remove spaces & convert to lowercase
    clean = s.replace(" ", "").lower()
    
    # check palindrome using slicing
    return clean == clean[::-1]


# Example
text = "A man a plan a canal Panama"
print(is_palindrome(text))
