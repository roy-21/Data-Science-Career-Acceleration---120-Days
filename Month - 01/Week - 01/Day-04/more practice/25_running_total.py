# Running total of list
nums = [5, 10, 15, 20]
running = []
total = 0

for n in nums:
    total += n
    running.append(total)

print("Running total:", running)
