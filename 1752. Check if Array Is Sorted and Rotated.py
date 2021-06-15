# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# Given an array nums, return true if the array was originally sorted in non-
# decreasing order, then rotated some number of positions (including zero).
# Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length
# such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

################################################################################

# count decrease times

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
            if count > 1:
                return False
        
        if count == 1:
            return nums[0] >= nums[-1]
        return True
