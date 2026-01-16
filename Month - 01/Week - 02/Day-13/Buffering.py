'''
DEEP DIVE: 13.7 Micro-Challenge: Buffering
Goal: Write 1 million lines. Why doesn't the disk spin 1 million times? 
Deep Dive: Python (and the OS) uses a **Buffer**. 
Data accumulates in RAM and is "Flushed" to disk in chunks to 
save I/O cycles.
'''

# Writing 1 million lines efficiently (buffered I/O)

with open("big_file.txt", "w", encoding="utf-8") as f:
    for i in range(1_000_000):
        f.write(f"Line {i}\n")
