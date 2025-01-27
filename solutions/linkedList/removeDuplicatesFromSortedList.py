"""
Problem: Remove Duplicates from Sorted List
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Approch: Iter on the list and remove duplicate if there is
Time Complexity: O(n)
Space Complexity: O(1)
"""

def deleteDuplicates(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    cur_node = head
    while cur_node and cur_node.next:
        if cur_node.val == cur_node.next.val:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next
    return head 

"""
Solution Explanation:
We iterate through the list. If the current node and its next node have the same value, we remove the next node by connecting the current node to the node after the next.
Otherwise, we move the current pointer to the next node.
It is important to maintain a reference to the head of the list throughout the process to ensure the result is correctly returned.
"""