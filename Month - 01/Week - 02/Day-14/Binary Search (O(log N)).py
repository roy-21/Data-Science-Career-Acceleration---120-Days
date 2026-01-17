'''
DEEP DIVE: 14.7 Capstone: Binary Search (O(log N))
Goal: Find index of number in sorted list. 
Deep Dive: Check middle. If too low, eliminate left half. If too high, 
eliminate right half. Repeat. Much faster than scanning.
'''
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1
