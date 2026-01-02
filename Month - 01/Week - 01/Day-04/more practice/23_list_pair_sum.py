# Find all pairs with given sum
nums = [2, 4, 3, 5, 7, 8]
target = 9

pairs = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print("Pairs:", pairs)
