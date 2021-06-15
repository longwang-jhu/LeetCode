# https://leetcode.com/problems/remove-element/

# Given an integer array nums and an integer val, remove all occurrences of val in
# nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you
# must instead have the result be placed in the first part of the array nums. More
# formally, if there are k elements after removing the duplicates, then the first
# k elements of nums should hold the final result. It does not matter what you
# leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the
# input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# If all assertions pass, then your solution will be accepted.

################################################################################

# in-place remove -> slow and fast ptrs

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return 0 if nums[0] == val else 1
        
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1 # only increase when different
            fast += 1
        return slow
                
