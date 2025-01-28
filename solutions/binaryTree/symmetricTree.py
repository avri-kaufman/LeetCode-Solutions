"""
Problem: Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/
Approch: Iterativ approch
Time Complexity: O(n)
Space Complexity: O(h) h = height of the tree
"""

def isSymmetric(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    l_s = [root]
    r_s = [root]
    left = root
    right = root
    while l_s and r_s:
        while left and right:
            if left.val != right.val:
                return False
            
            left = left.left
            right = right.right
            
            if left:
                l_s.append(left)
            if right:    
                r_s.append(right)
        if left or right:
            return False    
        left = r_s.pop()
        right = l_s.pop()
    return not l_s and not r_s  

"""
Solution Explanation:
We use two stacks for the left children and right children. We push the root to both of the stacks, and then, while the two stacks have some elements, we enter the inner while loop that iterates on the left and right branches of the tree and checks the equality of corresponding nodes.
After that, we will go to the right branch of the last node in the left branch and to the left branch of the last node in the right branch and do the same comparison. Each node is pushed to the stack so that we can iterate on its sub-nodes later.
If the values are not equal or there is a node without a corresponding node, we return False. If we check all nodes, we return True only if the stacks are empty.
"""