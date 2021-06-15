# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Given an integer array nums sorted in non-decreasing order, remove some
# duplicates in-place such that each unique element appears at most twice. The
# relative order of the elements should be kept the same.

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
