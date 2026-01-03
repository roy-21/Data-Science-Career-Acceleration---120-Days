# Rotate list
nums = [1,2,3,4,5]
k = 2

for _ in range(k):
    last = nums.pop()
    nums.insert(0, last)

print("Rotated list:", nums)
