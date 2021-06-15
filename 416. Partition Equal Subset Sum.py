# https://leetcode.com/problems/partition-equal-subset-sum/

# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.

################################################################################

# backpack with capacity = total / 2
# dp[i][j] = if nums[0...i-1] can reach j

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        
        n = len(nums)
        capacity = total // 2
        
        # base
        dp = [[False] * (capacity + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        
        # dp
        for i in range(1, n + 1):
            num = nums[i-1]
            for j in range(1, capacity + 1):
                dp[i][j] = dp[i-1][j] # do not use nums[i-1]
                if j >= num: # can use nums[i]
                    dp[i][j] = dp[i][j] or dp[i-1][j-num]
        
        return dp[-1][-1]
