# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array nums, remove the duplicates in-place such that each
# element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a
# modification to the input array will be known to the caller as well.

# Internally you can think of this:

###############################################################################

# in-place remove, sorted -> slow and fast ptrs

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1 # only increase when different
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1