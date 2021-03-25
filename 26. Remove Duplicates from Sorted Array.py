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

# use a slow ptr and modify it on the go
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow_ptr]:
                slow_ptr += 1
                nums[slow_ptr] = nums[i]
        return slow_ptr + 1