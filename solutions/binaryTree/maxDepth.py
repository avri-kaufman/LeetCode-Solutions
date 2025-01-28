"""
Problem: Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Approch: recursive
Time Complexity: O(n)
Space Complexity: O(h) h = height of the tree
"""

def maxDepth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0   

"""
Solution Explanation:
We use the recursive approach to calculate the maximum depth of the root's children plus one. If we encounter a null node, we return 0.
"""