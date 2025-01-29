"""
Problem: Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Approch: Two pointers
Time Complexity: O(len(t))
Space Complexity: O(1)
"""

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) > len(t):
        return False
    
    p_s = 0
    p_t = 0
    while p_s < len(s) and p_t < len(t):
        if s[p_s] == t[p_t]:
            p_s += 1
        p_t += 1
    return p_s == len(s)    

"""
Solution Explanation:
We use two pointers to check if the characters of s appear in t in the same order. First, we check if s is longer than t; if true, t cannot contain all the characters of s.
Otherwise, we iterate over t, and if we find the first character of s, we move the pointer of s to the next character and continue searching in t until we either reach the end of s or t.
If the pointer of s reaches the length of s, it means we have seen every character of s inside t in the correct order, so we return True. Otherwise, we reach the end of t without finding all characters of s.
"""