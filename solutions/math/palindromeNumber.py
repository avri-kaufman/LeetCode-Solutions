"""
Problem: Palindrom Number
Link: https://leetcode.com/problems/palindrome-number/
Approch: Check if the given number is palindorm 
Time Complexity: O(number of digits - log x base ten)
Space Complexity: O(number of digits - log x base ten)
"""
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if x < 0:
            return False
        rev = 0    
        while x:
            rev = rev * 10 + x % 10
            x = x // 10  
        return temp == rev 

"""
Solution Explanation:
The first naive approach is to convert the number into a string and then iterate over the string and its reverse to check if the original and reversed strings are equal.
This approach works, but we can solve the problem using only numbers, as the question suggests working with numeric types.
A better approach is to use division and modulo operations. The idea is to reverse the number using these operations and then check for equality between the reversed number and the original number.
"""