# Separate elements by index position
nums = [10,20,30,40,50,60]
even_index = []
odd_index = []

for i in range(len(nums)):
    if i % 2 == 0:
        even_index.append(nums[i])
    else:
        odd_index.append(nums[i])

print("Even index:", even_index)
print("Odd index:", odd_index)
