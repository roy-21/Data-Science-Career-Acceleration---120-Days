# Remove duplicates
data = [1,2,2,3,4,4,5]
unique = []

for d in data:
    if d not in unique:
        unique.append(d)

print("Unique list:", unique)
