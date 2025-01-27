"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Approch: Reconect the nodes, and create a new sorted list from the existing nodes
Time Complexity: O(n + m)
Space Complexity: O(1)
"""
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    m_list = ListNode()
    m_l_tail = m_list
    while list1 or list2:
        if list1 and list2:
            if list1.val < list2.val:
                m_l_tail.next, list1 = list1, list1.next
            else:
                m_l_tail.next, list2 = list2, list2.next        
        else:
            m_l_tail.next = list1 if list1 else list2
            break
        m_l_tail = m_l_tail.next     
    return m_list.next

"""
Solution Explanation:
The naive approach is to create a new list that will contain new nodes. We iterate through the two lists, compare their node values, and insert the smaller value into the new list.
This approach has linear space complexity, but we can do better by reconstructing the references of the two lists into a single list based on the comparisons.
We also need to handle cases where one list is shorter than the other. In such cases, we attach the remaining nodes of the longer list to the tail of the reconstructed list.
"""