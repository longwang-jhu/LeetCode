# https://leetcode.com/problems/minimum-path-sum/

# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

###############################################################################

# dp[m][n] = min sum from top left to (m,n)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_col, n_row = len(grid[0]), len(grid)
        
        dp = [[0 for _ in range(n_col)] for _ in range(n_row)]
        dp[0][0] = grid[0][0]

        # initialize first col
        for i in range(1, n_row):
            dp[i][0] = dp[i-1][0] + grid[i][0]      
        
        # initialize first row
        for j in range(1, n_col):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # loop for the row and col
        for i in range(1, n_row):
            for j in range(1, n_col):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]