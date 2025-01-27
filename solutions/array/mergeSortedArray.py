"""
Problem: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Approch: Merge from the end of the arrays into nums1
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n:
            n_1 = nums1[m - 1] if m else 0
            n_2 = nums2[n - 1]
            if n_1 > n_2 and m:
               nums1[n + m - 1] = n_1
               m -= 1
            else:
                nums1[n + m - 1] = n_2
                n -= 1      
        return nums1 

"""
Solution Explanation:
The problem asks to merge nums2 into nums1 and maintain ascending order after merging.
A naive approach is to iterate over the arrays from the smallest elements, comparing elements from nums1 and nums2. Then, place the smaller element into nums1.
This approach causes complications when inserting elements from nums2 into nums1. Specifically, we need to temporarily store the elements of nums1 somewhere.
Initially, I thought about storing them at the tail of nums1, but this leads to significant storage management issues.
Additionally, we would need to compare three elements: the head of nums1, the tail of nums1, and the head of nums2. This is not an efficient approach.
If we want to store the nums1 elements somewhere else, it could lead to a worst-case space complexity of O(m), which is not ideal since we can achieve better performance.
A more efficient approach is to start from the largest elements in nums1 and nums2 and merge the arrays from the end. This approach simplifies the comparison process,
maintains linear time complexity O(n + m), and achieves constant space complexity O(1).
"""
