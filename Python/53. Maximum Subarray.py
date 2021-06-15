# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.

###############################################################################

# nums -> prefix_sums
# track min_val and update max_sum

# dp[i] = max_sum of subarray ending at nums[i]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return self.greedy(nums)
        return self.dp(nums)
    
    def greedy(self, nums):
        if len(nums) == 1: return nums[0]
        
        n = len(nums)
        prefix_sums = nums # convert to prefix sums
        for i in range(1, n):
            prefix_sums[i] += prefix_sums[i-1]
        
        # recall stock trading problem
        max_sum = prefix_sums[0]
        min_val = 0 # subarray may have just one one number
        for i in range(n):
            max_sum = max(max_sum, prefix_sums[i] - min_val)
            min_val = min(min_val, prefix_sums[i]) # update min_val

        return max_sum
    
    def dp(self, nums):
        if len(nums) == 1: return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0] # base case
        for i in range(1, n):
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)