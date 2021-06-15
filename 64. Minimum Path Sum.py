# https://leetcode.com/problems/minimum-path-sum/

# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

################################################################################

# dp[m][n] = min_sum to (m,n)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # base
        dp[0][0] = grid[0][0]
        for i in range(1, m): # first col
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n): # first row
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # loop over row and col
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]
