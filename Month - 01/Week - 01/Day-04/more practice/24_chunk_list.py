# Split list into chunks
data = list(range(1, 21))
size = 5
chunks = []

for i in range(0, len(data), size):
    chunks.append(data[i:i+size])

print("Chunks:", chunks)
