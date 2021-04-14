# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.

###############################################################################

# nums -> prefix_sums
# track min_val and update max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0 
        if len(nums) == 1: return nums[0]
        
        n = len(nums)
        prefix_sums = nums # convert to cum_sum
        for i in range(1, n):
            prefix_sums[i] += prefix_sums[i-1]
        
        # recall stock trading problem
        max_sum = float('-inf') # subarray needs at least one number
        min_val = 0
        for i in range(n):
            max_sum = max(max_sum, prefix_sums[i] - min_val)
            min_val = min(min_val, prefix_sums[i]) # update min_val

        return max_sum