# https://leetcode.com/problems/remove-element/

# Given an array nums and a value val, remove all instances of that value in-
# place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a
# modification to the input array will be known to the caller as well.

# Internally you can think of this:

###############################################################################

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
                