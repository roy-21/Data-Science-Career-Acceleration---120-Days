# Reverse list without method
nums = [1,2,3,4,5]
reversed_list = []

for i in range(len(nums)-1, -1, -1):
    reversed_list.append(nums[i])

print("Reversed:", reversed_list)
