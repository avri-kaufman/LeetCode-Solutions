"""
Problem: Same Tree
Link: https://leetcode.com/problems/same-tree/
Approch: Check equality recursively for every sub tree
Time Complexity: O(min(n,m))
Space Complexity: O(1)
"""

def isSameTree(self, p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """
    if not (p or q):
        return True
    elif p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:    
        return False   

"""
Solution Explanation:
We will check that the curr heads have the same value and recursively their sub trees
"""