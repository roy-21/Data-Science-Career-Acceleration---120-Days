'''
DEEP DIVE: 13.6 Micro-Challenge: CSV Parsing
Goal: Read a CSV into a list of dictionaries. 
Deep Dive: Use csv. DictReader. It han-dles quoted strings and 
delimiters automatically, preventing bugs when data contains commas.
'''

import os
import csv

# Option 1: Absolute path (replace with your file location)
csv_path = r'e:\path\to\your\data.csv'  # Use raw string for Windows paths

# Option 2: Check if file exists first
if os.path.exists('data.csv'):
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    print(data)
else:
    print("File 'data.csv' not found! Check path or create sample file.")


