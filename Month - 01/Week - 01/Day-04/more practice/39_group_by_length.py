# Group strings by length
words = ["hi", "cat", "apple", "dog", "banana"]
groups = {}

for w in words:
    l = len(w)
    if l not in groups:
        groups[l] = []
    groups[l].append(w)

print("Groups:", groups)
