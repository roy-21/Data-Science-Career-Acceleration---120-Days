# Swap adjacent elements
nums = [1,2,3,4,5,6]

for i in range(0, len(nums)-1, 2):
    nums[i], nums[i+1] = nums[i+1], nums[i]

print("Swapped list:", nums)
