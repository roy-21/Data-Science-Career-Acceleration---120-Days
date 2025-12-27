# Count vowels in a string
text = "python programming"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)
