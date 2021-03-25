# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?

###############################################################################

# dp[i] =  distinct ways to level i-1
# dp[i] = dp[i-1] + dp[i-2]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]