# https://leetcode.com/problems/jump-game/

# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Determine if you are able to reach the last index.

###############################################################################

# dp[i] = if can reach idx i

# greedy: start from end, determine if can move back to beginning

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ### dp ###
        n = len(nums)
        if n == 1:
            return True
        
        dp = [False for _ in range(n)]
        dp[0] = True
        
        for i, jump in enumerate(nums):
            if dp[i] == True:
                if i + jump >= n - 1: # reach the end
                    return True
                else:
                    dp[i + 1:i + jump + 1] = [True] * jump
            else:
                return False
        
        ### greedy ###
        n = len(nums)
        last_pos = n - 1
        
        for i in range(n-1, -1, -1): # loop backwards
            if i + nums[i] >= last_pos: # determine if can jump to last position
                last_pos = i
        
        return last_pos == 0 # determine if can reach the beginning