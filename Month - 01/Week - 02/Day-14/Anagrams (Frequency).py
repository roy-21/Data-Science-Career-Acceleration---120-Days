'''
DEEP DIVE: 14.3 Capstone: Anagrams (Frequency)
Goal: Are "silent" and "listen" anagrams? 
Deep Dive: 1. Sort both (O(N log N)). 
2.Count frequencies: {'s':1, 'i':1... (O(N)). Use collections.Counter.
'''

from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
    # Alternatively, using sorting:
    # return sorted(s) == sorted(t) 