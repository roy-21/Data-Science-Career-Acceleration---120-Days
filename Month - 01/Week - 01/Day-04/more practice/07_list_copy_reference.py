# copy vs reference
a = [1, 2, 3]
b = a
c = a.copy()

a.append(4)

print("a:", a)
print("b:", b)
print("c:", c)
