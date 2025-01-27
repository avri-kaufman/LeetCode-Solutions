"""
Problem: Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Approch: Travers the tree by recursion or by stuck
Time Complexity: O(n)
Space Complexity: O(h) h = hight of the tree
"""

def inorderTraversal(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    if not root:
        return []
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 

# solution without recursion
def inorderTraversal(root):
    ans = []
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right
    return ans  

"""
Solution Explanation:
We can traverse the tree either using recursion or by maintaining a stack manually. In both approaches,
the time will remain linear and space will be proportional to the height of the tree.
This is because, at any point, the maximum number of recursive calls or elements in the stack will depend on the height of the tree.
"""