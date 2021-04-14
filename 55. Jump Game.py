# https://leetcode.com/problems/jump-game/

# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Determine if you are able to reach the last index.

###############################################################################

# jump -> curr depends on prev -> dp
# dp[i] = if can reach nums[0, ..., i]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1: return True

        n = len(nums)
        dp = [False for _ in range(n)]
        dp[0] = True
        
        for i, jump in enumerate(nums):
            if dp[i]:
                if i + jump >= n - 1: # reach the end
                    return True
                else:
                    dp[i + 1:i + jump + 1] = [True] * jump
            else:
                return False

# greedy: start from end, determine if can move back to beginning

    def canJump2(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1: return True

        n = len(nums)
        frontier = n - 1
        
        for i in range(n - 1, -1, -1): # move backwards
            if i + nums[i] >= frontier: # determine if can jump to frontier
                frontier = i
        
        return frontier == 0 # determine if can reach the beginning