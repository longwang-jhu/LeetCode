# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?

###############################################################################

# use binary search to find starting and ending position seperately

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        
        # find starting position
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        
        if nums[left] == target:
            ans_start = left
        elif nums[right] == target:
            ans_start = right
        else:
            ans_start = -1
        
        # find ending position
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        
        if nums[right] == target:
            ans_end = right
        elif nums[left] == target:
            ans_end = left
        else:
            ans_end = -1
        
        return [ans_start, ans_end]