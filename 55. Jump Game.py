# https://leetcode.com/problems/jump-game/

# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Determine if you are able to reach the last index.

###############################################################################

# dp[i] = if can reach nums[i]

# greedy: start from end, determine if can move backwards

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return self.jump_dp(nums)
        return self.greedy(nums)
            
    def jump_dp(self, nums):
        n = len(nums)
        if n == 1: return True

        # init
        dp = [False] * n
        dp[0] = True
        
        for i in range(n):
            jump = nums[i]
            if dp[i]: # jump forwards
                if i + jump >= n - 1: # reach the end
                    return True
                else:
                    dp[i + 1 : i + jump + 1] = [True] * jump
            else:
                return False    

    def greedy(self, nums):
        n = len(nums)
        if n == 1: return True
        
        frontier = n - 1       
        for i in range(n - 1, -1, -1): # move backwards
            if i + nums[i] >= frontier: # determine if can jump to frontier
                frontier = i
        
        return frontier == 0 # determine if can reach the beginning