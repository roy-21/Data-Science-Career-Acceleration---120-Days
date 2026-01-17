'''
DEEP DIVE: 14.8 Capstone: Missing Number (Math)
Goal: List 1 to 100 is missing one number. Find it. 
Deep Dive: Don't scan. Calculate Expected Sum NON+1), Subtract Actual 
Sum. The difference is the missing number.
'''

def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
