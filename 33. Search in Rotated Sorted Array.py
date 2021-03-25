# https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct
# values).

# Prior to being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
# [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.

###############################################################################

# binary search: [first part | second part]
# determine which part mid is in

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[mid]: # mid is in the first part
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else: # mid is in the second part
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1