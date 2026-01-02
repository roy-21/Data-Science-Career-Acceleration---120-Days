# Find missing number from sequence
nums = [1,2,3,5,6]
n = 6

missing = []
for i in range(1, n+1):
    if i not in nums:
        missing.append(i)

print("Missing numbers:", missing)
