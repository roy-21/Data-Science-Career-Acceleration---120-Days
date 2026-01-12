'''
11.5 Micro-Challenge: The Custom Sort Key
Goal: Sort ["100px", "20px", "3px"] numerically (so 3px comes first). 
Deep Dive: sorted(data, key-lambda x: int(x[:-2])). The key function 
transforms the item only for comparison purposes, leaving the original 
data intact.
'''

values = ["100px", "20px", "3px"]

sorted_values = sorted(values, key=lambda x: int(x[:-2]))

print(sorted_values)
