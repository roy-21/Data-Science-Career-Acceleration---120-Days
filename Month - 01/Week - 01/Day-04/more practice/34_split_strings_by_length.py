# Split strings by length
words = ["apple", "hi", "banana", "cat", "elephant"]
short = []
long = []

for w in words:
    if len(w) <= 3:
        short.append(w)
    else:
        long.append(w)

print("Short words:", short)
print("Long words:", long)
