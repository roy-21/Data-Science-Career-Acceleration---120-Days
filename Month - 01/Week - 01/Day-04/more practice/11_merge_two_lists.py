# Merge two lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged = []
i = j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

merged.extend(list1[i:])
merged.extend(list2[j:])

print("Merged list:", merged)
