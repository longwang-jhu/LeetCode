# https://leetcode.com/problems/counting-bits/

# Given an integer n, return an array ans of length n + 1 such that for each i (0
# <= i <= n), ans[i] is the number of 1's in the binary representation of i.

################################################################################

# dp[i] = dp[i >> 1] + (i & 1)

class Solution:
    def countBits(self, num: int) -> List[int]:
        # init
        dp = [None] * (num + 1)
        dp[0] = 0
        
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
