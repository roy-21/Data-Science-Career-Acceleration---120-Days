# Flatten nested list
nested = [[1,2],[3,4],[5,6]]
flat = []

for sub in nested:
    for item in sub:
        flat.append(item)

print("Flattened list:", flat)
