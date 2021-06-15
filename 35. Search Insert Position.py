# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, return the index
# if the target is found. If not, return the index where it would be if it were
# inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

################################################################################

# find target, sorted -> binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0: return 0
        if nums[0] > target: return 0
        if nums[-1] < target: return len(nums)
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else: # nums[mid] < target
                left = mid
        
        # left <= target <= right
        if nums[left] == target:
            return left
        else: # nums[right] >= target:
            return right
