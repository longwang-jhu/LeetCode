# https://leetcode.com/problems/unique-paths-ii/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).

# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?

# An obstacle and space is marked as 1 and 0 respectively in the grid.

###############################################################################

# curr depends on prev -> dp
# dp[m][n] = unique path to reach (m, n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        # initialize
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1

        for i in range(1,m): # first column
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
                
        for j in range(1,n): # first row
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        
        # loop over row and column
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]