'''
DEEP DIVE: 13.9 Micro-Challenge: Custom Context Manager
Goal: Create a block with Timer(): that prints time taken. 
Deep Dive: Implement __enter (start timer) and __exit (end timer).
'''

import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self  # Optional: allows 'as timer' access
    
    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f'Time taken: {elapsed:.4f} seconds')
