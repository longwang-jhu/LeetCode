# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).

# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).

# How many possible unique paths are there?

###############################################################################

# dp[m][n] = unique path to reach (m,n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # initialize
        dp[0][0] = 1
        # initialize first column
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]
        # initialize first row
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]
        
        # loop over each row
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]