# Sum of nested list
matrix = [[1,2,3], [4,5,6], [7,8,9]]

total = 0
for row in matrix:
    for value in row:
        total += value

print("Matrix sum:", total)
