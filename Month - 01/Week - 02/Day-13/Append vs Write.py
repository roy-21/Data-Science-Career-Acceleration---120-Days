'''
DEEP DIVE: 13.2 Micro-Challenge: Append vs Write
Goal: Add a log line to a file without deleting old content. 
Deep Dive: Mode 'w' wipes the file. Mode 'a' appends to the end. 
Mode 'x' fails if file exists (Safety).
'''

# Appending a log line without deleting old content

with open("app.log", "a") as f:
    f.write("INFO: Application started successfully\n")
