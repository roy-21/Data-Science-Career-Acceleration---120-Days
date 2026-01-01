# Rotate list by N positions
nums = [1,2,3,4,5]
n = 3

for _ in range(n):
    nums.insert(0, nums.pop())

print("Rotated:", nums)
