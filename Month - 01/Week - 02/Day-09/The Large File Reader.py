'''
DEEP DIVE: 9.7 Micro-Challenge: The Large File Reader
Goal: Write a generator to read a "fake" 100GB file line-by-line. 
Deep Dive: Using yield line allows you to process datasets larger than 
your machine's physical RAM. This is the standard 
for Big Data processing in Python.
'''

# Simulated large file generator (no real file)

def fake_large_file_reader():
    line_number = 1
    while True:
        yield f"This is line {line_number}"
        line_number += 1


# Read only first 10 lines (otherwise infinite)
for i, line in enumerate(fake_large_file_reader()):
    if i == 10:
        break
    print(line)

