'''
DEEP DIVE: 8.4 Micro-Challenge: The Queue Bottleneck (Pop)
Goal: Compare list.pop() vs list.pop(0). Deep Dive: .pop() removes the 
last item (0(1))..pop (0) removes the first item, requiring a Left Shift 
of all remaining items to fill the gap (O(N)). Fix: Use collections.
deque for fast First-In-First-Out queues.
'''

from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.popleft()   # Remove first element in O(1)
dq.pop()       # Remove last element in O(1)
print(dq)