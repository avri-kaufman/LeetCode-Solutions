"""
Problem: Plus One
Link: https://leetcode.com/problems/plus-one/
Approch:Increment the first non-9 digit, or flip every 9 digit to 0 until you encounter a non-9 digit or reach the first index in the array.
Time Complexity: O(n)
Space Complexity: O(1)
"""


def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    i = len(digits) - 1
    while True:
        if i == - 1:
            digits.insert(0, 1)
            break
        elif digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
        i -= 1    
    return digits   

"""
Solution Explanation:
Increment the first non-9 digit, or flip every 9 digit to 0 until you encounter a non-9 digit or reach the first index in the array.
"""