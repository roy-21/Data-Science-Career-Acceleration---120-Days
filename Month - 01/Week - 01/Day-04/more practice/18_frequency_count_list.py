# Frequency count
data = ["a","b","a","c","b","a"]
unique = []

for item in data:
    if item not in unique:
        unique.append(item)

for u in unique:
    count = 0
    for d in data:
        if d == u:
            count += 1
    print(u, "=>", count)
