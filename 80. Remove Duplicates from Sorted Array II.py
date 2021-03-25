# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array; you must do this by modifying
# the input array in-place with O(1) extra memory.

# Clarification:

# Confused why the returned value is an integer, but your answer is an array?

# Note that the input array is passed in by reference, which means a
# modification to the input array will be known to the caller.

# Internally you can think of this:

###############################################################################

# use slow_ptr and count number of duplicates

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_ptr = 0
        count = 0 # count for dulicates
        for i in range(1, len(nums)):
            if nums[i] != nums[slow_ptr]: # no duplicate
                slow_ptr += 1
                nums[slow_ptr] = nums[i]
                count = 0
            elif count == 0: # duplicate, but the first time
                slow_ptr += 1
                nums[slow_ptr] = nums[i]
                count += 1
        
        return slow_ptr + 1