"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Approch: Validation the parentheses whit stuck ds 
Time Complexity: O(n)
Space Complexity: O(1)
"""

def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if stack:
                    b = stack.pop()
                    if brackets[b] != c:
                        return False
                else:
                    return False        
        return not stack     

"""
Solution Explanation:
We iterate over the string. If we encounter an open bracket, we insert it into the stack. If we encounter a closing bracket, we pop from the stack and check if the current bracket matches the closing bracket of the popped one. If it does not, we return false.
At the end, we check if the stack is empty. If it is not, it means there are open brackets without matching closing brackets, and we return false. Otherwise, we return true."""