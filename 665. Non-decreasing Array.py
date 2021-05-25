# https://leetcode.com/problems/non-decreasing-array/

# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).

###############################################################################

# greedy

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 2: return True
        
        n = len(nums)
        is_modified = False
        for i in range(1, n):
            if nums[i-1] > nums[i]: # found a violation
                if is_modified:
                    return False
                is_modified = True
                
                if i == 1 or nums[i-2] <= nums[i]: # change nums[i-1]
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1] # change nums[]
        
        return True