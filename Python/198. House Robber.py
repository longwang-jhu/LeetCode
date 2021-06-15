# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.

###############################################################################

# dp[i] = max money in nums[0...i-1]
# dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        # base
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        
        # dp
        for i in range(2, n + 1):
            dp[i] = max(dp[i-1], # not rob nums[i-1]
                        dp[i-2] + nums[i-1]) # rob nums[i-1]
        
        return dp[-1]