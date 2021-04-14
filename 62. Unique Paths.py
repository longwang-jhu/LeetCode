# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).

# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).

# How many possible unique paths are there?

###############################################################################

# curr depends on prev -> dp
# dp[m][n] = unique path to reach (m, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: return 0
        if m == 1 or n == 1: return 1
        
        dp = [[0] * n for _ in range(m)]
        
        # initialize
        dp[0][0] = 1
        for i in range(1,m):
            dp[i][0] = 1
        for j in range(1,n):
            dp[0][j] = 1
        
        # loop over row and column
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]