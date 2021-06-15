# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.

###############################################################################

# binary search: [first part | second part]
# set right -= 1 if cannot decide which part mid is in

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[right]: # mid is in the first part
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[right]: # mid is in the second part
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                right -= 1
        
        return nums[left] == target or nums[right] == target