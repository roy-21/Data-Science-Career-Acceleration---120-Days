# Split positive and negative numbers
numbers = [10, -5, 7, -3, 0, 4]

positive = []
negative = []

for n in numbers:
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)

print("Positive:", positive)
print("Negative:", negative)
