# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?

###############################################################################

# find target, sorted -> binary search
# find start_idx, end_idx seperately

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0: return [-1, -1]
        if len(nums) == 1: return [0, 0] if nums[0] == target else [-1, -1]
        
        n = len(nums)
        
        # find start_idx
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else: # nums[mid] < target
                left = mid        
        if nums[left] == target:
            start_idx = left
        elif nums[right] == target:
            start_idx = right
        else:
            start_idx = -1
        
        # find end_idx
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else: # nums[mid] > target
                right = mid
        
        if nums[right] == target:
            end_idx = right
        elif nums[left] == target:
            end_idx = left
        else:
            end_idx = -1
        
        return [start_idx, end_idx]