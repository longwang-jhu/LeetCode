# https://leetcode.com/problems/combination-sum-iv/

# Given an array of distinct integers nums and a target integer target, return the
# number of possible combinations that add up to target.

# The answer is guaranteed to fit in a 32-bit integer.

################################################################################

# dp[i] = ways to get sum i
# update: dp[i] = sum dp[i - nums[j]] over j

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # init
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        
        # dp
        for i in range(1, target + 1):
            for j in range(n):
                if nums[j] <= i: # use nums[j]
                    dp[i] += dp[i - nums[j]]
        return dp[-1]
                    
