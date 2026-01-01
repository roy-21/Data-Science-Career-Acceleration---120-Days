# Squares and cubes lists
nums = [1,2,3,4,5]
squares = []
cubes = []

for n in nums:
    squares.append(n*n)
    cubes.append(n*n*n)

print("Squares:", squares)
print("Cubes:", cubes)
