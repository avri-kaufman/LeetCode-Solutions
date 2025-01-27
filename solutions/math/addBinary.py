"""
Problem: Add Binary
Link: https://leetcode.com/problems/add-binary/
Approch: Iter over the binary numbers and add their digits with the last carry
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    ans = ''
    p_a = len(a) - 1
    p_b = len(b) - 1
    carry = 0
    new_digit = 0
    while p_a >= 0 or p_b >= 0:
        a_dig = 0 if p_a < 0 else int(a[p_a])
        b_dig = 0 if p_b < 0 else int(b[p_b])
        new_digit = (carry + a_dig + b_dig) % 2
        carry = (carry + a_dig + b_dig) // 2
        p_a -= 1
        p_b -= 1
        ans = str(new_digit) + ans
    return ans if carry == 0 else '1' + ans

"""
Solution Explanation:
Iterate through the digits of the numbers from the least significant bit to the most significant bit,
storing the carry. The new digit will be the modulus of the sum of the digits with the current carry,
and the new carry will be the division of the sum of the three digits.
"""