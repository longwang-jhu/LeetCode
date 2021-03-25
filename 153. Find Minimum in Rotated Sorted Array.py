# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.

###############################################################################

# binary search: [first part | second part]
# determine which part mid is in

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # mid is in the first part
                left = mid
            else: # num[mid] < mid[right], mid is in the second part
                right = mid
        
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]