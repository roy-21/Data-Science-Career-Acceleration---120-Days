# Difference of two lists
a = [1,2,3,4,5]
b = [3,4]

diff = []
for x in a:
    if x not in b:
        diff.append(x)

print("Difference:", diff)
