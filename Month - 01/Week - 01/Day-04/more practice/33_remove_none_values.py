# Remove None values
data = [1, None, 2, None, 3, 4]

cleaned = []
for x in data:
    if x is not None:
        cleaned.append(x)

print("Cleaned list:", cleaned)
