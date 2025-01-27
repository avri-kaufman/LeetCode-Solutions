"""
Problem: Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/
Approch: Start with the first string as the lognest common prefix and pron it base on the other strings in the arr
Time Complexity: O(n * m)
Space Complexity: O(n)
n = len of first string
m = num of strings in the arr
"""

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pr = strs[0]
        for s in strs:
            pr = pr[0: self.getLastIndexOfEquality(s, pr)]
        return pr

def getLastIndexOfEquality(self, a, b):
    i = 0
    while i < min(len(a), len(b)):
        if a[i] != b[i]:
            break
        i = i + 1    
    return i    

"""
Solution Explanation:
The idea is that the longest common prefix can be at most the first string in the array.
Therefore, we start with the first string and iteratively shorten it based on the other strings in the array.
"""