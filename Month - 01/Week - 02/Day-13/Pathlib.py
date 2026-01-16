'''
DEEP DIVE: 13.8 Micro-Challenge: Pathlib
Goal: Join a folder and filename safely on Windows and Mac. 
Deep Dive: Do not use string concatenation folder + "/" + file. 
Use pathlib. Path. It handles OS-specific separators (\vs/) 
automatically.
'''

from pathlib import Path

folder = Path("data")          
filename = "results.csv"     

# Method 1: Forward slash operator (recommended)
full_path1 = folder / filename  
print(full_path1)  

# Method 2: joinpath() method
full_path2 = folder.joinpath(filename)
print(full_path2)  # Identical result
