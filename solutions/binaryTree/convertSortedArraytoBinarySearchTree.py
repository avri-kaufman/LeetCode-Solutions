"""
Problem: Convert Sorted Array to Binary Search Tree
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Approch: Recursive approch
Time Complexity: O(n)
Space Complexity: O(log n)
"""


def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: Optional[TreeNode]
    """
    def helper(l, r):
        if l > r:
            return
        mid = (l + r) // 2  
        tree = TreeNode(val=nums[mid])
        tree.right = helper(mid + 1, r)
        tree.left = helper(l, mid - 1)
        return tree
    return helper(0, len(nums) - 1)      

"""
Solution Explanation:
We build the BST with recursion on the left and right sub trees.
"""