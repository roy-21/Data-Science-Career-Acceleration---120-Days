# Filtering list
ages = [12, 18, 25, 10, 30, 16]
adults = []

for age in ages:
    if age >= 18:
        adults.append(age)

print("Adults:", adults)
