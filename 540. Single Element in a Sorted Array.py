# https://leetcode.com/problems/single-element-in-a-sorted-array/

# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once. Find
# this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

################################################################################

# check if mid % 2 == 0
# if even, check nums[mid] == nums[mid + 1]
# if odd, check nums[mid] == nums[mid - 1]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if mid % 2 == 0: # mid if even
                if nums[mid] == nums[mid + 1]: # single num is on right
                    left = mid + 2
                else:
                    right = mid
            else: # mid if odd
                if nums[mid] == nums[mid - 1]: # single num is on right
                    left = mid + 1
                else:
                    right = mid
        
        if right == len(nums) - 1:
            return nums[right] if nums[left] == nums[left - 1] else nums[left]
        else:
            return nums[left] if nums[right] == nums[right + 1] else nums[right]
