# Left shift list
nums = [1,2,3,4,5]
k = 2

for _ in range(k):
    first = nums.pop(0)
    nums.append(first)

print("Left shifted:", nums)
