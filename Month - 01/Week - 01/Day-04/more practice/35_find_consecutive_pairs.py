# Find consecutive increasing pairs
nums = [1,2,3,5,6,8,9]

pairs = []
for i in range(len(nums)-1):
    if nums[i+1] == nums[i] + 1:
        pairs.append((nums[i], nums[i+1]))

print("Consecutive pairs:", pairs)
