# https://leetcode.com/problems/jump-game-ii/

# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

###############################################################################

# dp[i] = minimum jumps to reach pos i
# record last_pos, update when can go beyond last_pos

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        dp = [0 for _ in range(n)]
        last_pos = 0
        
        for i, jump in enumerate(nums):
            new_last_pos = i + jump
            if new_last_pos >= n - 1: # reach the end
                return dp[i] + 1
            elif new_last_pos > last_pos: # can go beyond
                dp[last_pos + 1:new_last_pos + 1] = [dp[i] + 1] * (new_last_pos - last_pos)
                last_pos = new_last_pos