# https://leetcode.com/problems/jump-game-ii/

# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

###############################################################################

# jump -> curr depends on prev -> dp
# dp[i] = min jumps to reach nums[0, ..., i]
# record frontier

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1: return 0
        
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        frontier = 0
        
        for i, jump in enumerate(nums):
            new_pos = i + jump
            if new_pos >= n - 1: # reach the end
                return dp[i] + 1
            elif new_pos > frontier: # can go further
                # update dp[frontier+1, ..., new_pos] = dp[i] + 1
                dp[frontier + 1:new_pos + 1] = [dp[i] + 1] * (new_pos - frontier)
                frontier = new_pos