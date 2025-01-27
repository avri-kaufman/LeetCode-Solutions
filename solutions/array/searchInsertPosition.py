"""
Problem: Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Approch: Use binary search to find the insert position
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0 
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
        else:
            start = mid + 1
    
    if target > nums[start]:
        return start + 1
    else:
        return start   
  

"""
Solution Explanation:
We use binary search to find the position of the target in the array. If the target exists in the array, we return its index.
If the target is not found, we check whether the last element encountered during the search is larger or smaller than the target.
If it is larger, the target should be placed at that position. If it is smaller, the target should be placed in the next position.
"""