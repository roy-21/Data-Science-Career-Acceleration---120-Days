# Shopping cart
prices = [120, 250, 75, 300]
total = 0

for p in prices:
    total += p

print("Total bill:", total)

if total > 500:
    print("Discount applied")
else:
    print("No discount")
