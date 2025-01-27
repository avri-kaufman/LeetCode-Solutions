"""
Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Approch: We can use two pointers one for the curr val that we check and the other for the free space
Time Complexity: O()
Space Complexity: O()
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last_unique = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[last_unique + 1] = nums[i]
            last_unique += 1
    return last_unique + 1

"""
Solution Explanation:
To solve the problem, we will use two pointers. The space between the pointers represents a window of non-unique values that we can 
overwrite. Unique values will be placed at the head of the array, while the tail will contain the non-unique
values that we encounter.
We iterate through the array. If the value we see is unique, we store it in the first available position for unique values.
If it is not unique, we simply continue and overwrite it later with another unique value.
"""
