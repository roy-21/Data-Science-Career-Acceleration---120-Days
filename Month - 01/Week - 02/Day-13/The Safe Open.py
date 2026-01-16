'''
Persistence (Files & Contexts)

DEEP DIVE: 13.1 Micro-Challenge: The Safe Open
Goal: Write to a file without.close(). 
Deep Dive: Use with open(...) as f. This is a Context Manager. 
It guarantees file closure even if an exception crashes the block.
'''

with open("example.txt", "w") as f:
    f.write("Hello, this file was written safely using a context manager!\n")
    f.write("No need to call close() manually.")
