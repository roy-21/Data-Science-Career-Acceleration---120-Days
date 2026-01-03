# Find max and min
numbers = [45, 12, 89, 23, 67]

max_val = numbers[0]
min_val = numbers[0]

for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Max:", max_val)
print("Min:", min_val)
