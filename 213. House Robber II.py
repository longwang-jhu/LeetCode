# https://leetcode.com/problems/house-robber-ii/

# You are a professional robber planning to rob houses along a street. Each house
# has a certain amount of money stashed. All houses at this place are arranged in
# a circle. That means the first house is the neighbor of the last one. Meanwhile,
# adjacent houses have a security system connected, and it will automatically
# contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.

################################################################################

# rob nums[:-1] or nums[1:]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))
    
    def rob_helper(self, nums):
        # init
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        
        # dp
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        
        return dp[-1]
            
