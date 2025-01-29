"""
Problem: Minimum Depth of Binary Tree
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Approch: Recursive approch
Time Complexity: O(n)
Space Complexity: O(h) h = height of the tree
"""

def minDepth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif root.left and root.right:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    return 1 + minDepth(root.left) if root.left else 1 + minDepth(root.right)   

"""
Solution Explanation:
We use a recursive approach to get the minimum height of the tree. The key point is that a leaf node has no children,
so we need to get the minimum height of a node that has no children.
We first check if there is a root. If there are no children, we return 1 as we have reached a leaf node.
Otherwise, if there are two children, we take the minimum height of the children. Finally, if there is one child, we take its height.
"""