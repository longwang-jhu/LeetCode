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

# dp[m][n] = unique path to reach (m,n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])       
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # initialize
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1

        # initialize first column
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
                
        # initialize first row
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        
        # loop over each row
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]