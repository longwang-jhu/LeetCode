# https://leetcode.com/problems/maximum-ascending-subarray-sum/

# Given an array of positive integers nums, return the maximum possible sum of
# an ascending subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
# where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is
# ascending.

###############################################################################

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        curr_sum = nums[0]
        ans = curr_sum
        
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i] # reset curr_sum
            
            ans = max(ans, curr_sum)
            i += 1
                
        return ans