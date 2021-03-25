# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.

###############################################################################

# binary search: [first part | second part]
# set right -= 1 if cannot decide which part mid is in

# linear search: look for the first number < nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # mid is in the first part
                left = mid
            elif nums[mid] < nums[right]: # mid is in the second part
                right = mid
            else:
                right -= 1
        
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
        
        # linear search
        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] < ans:
                return nums[i]
        return ans