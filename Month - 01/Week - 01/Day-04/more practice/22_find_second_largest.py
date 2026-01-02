# Find second largest number
nums = [10, 45, 23, 89, 67]

largest = second = -1
for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Largest:", largest)
print("Second Largest:", second)
