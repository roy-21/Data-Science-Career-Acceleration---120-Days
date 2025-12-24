'''
DEEP DIVE: 8.1 Micro-Challenge: The Linear Scan (O(N))
Goal: Create a list of 10 million numbers. Check if -5 is in the list. 
Deep Dive: Python performs a Linear Search. It loads index 0, compares, 
loads index 1, compares... all the way to 10 million. Complexity: O(N). 
If data doubles, time doubles.
'''
def linear_search():
    number = list(range(10000000))
    if -5 in number:
        return True
    else:
        return False
    
print(linear_search())

#This function performs a linear scan over N elements to check membership,
#so the time complexity is O(N).