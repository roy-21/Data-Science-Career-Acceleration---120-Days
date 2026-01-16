'''
DEEP DIVE: 13.4 Micro-Challenge: Encoding Hell
Goal: Fix a "UnicodeDecodeError". 
Deep Dive: Always specify encoding='utf-8'. 
Windows defaults to 'cp1252', which crashes on emojis or foreign 
characters.
'''

# Create the file with UTF-8 content

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello 😊\nworld\n")

# Then read it safely
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())


