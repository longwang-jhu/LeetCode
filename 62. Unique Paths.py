# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
# diagram below).

# The robot can only move either down or right at any point in time. The robot is
# trying to reach the bottom-right corner of the grid (marked 'Finish' in the
# diagram below).

# How many possible unique paths are there?

################################################################################

# dp[m][n] = unique path to reach (m, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1

        # init
        dp = [[1] * n for _ in range(m)]
        
        # dp: loop over row and column
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
        return dp[-1][-1]
