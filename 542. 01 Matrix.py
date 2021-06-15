# https://leetcode.com/problems/01-matrix/

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each
# cell.

# The distance between two adjacent cells is 1.

################################################################################

# dp -> search from top-left and then from bottom-right

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat: return mat
        
        m, n = len(mat), len(mat[0])
        dp = [[float('inf')] * n for _ in range(m)]
        
        # search from top-left
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i == 0 and j != 0:
                        dp[i][j] = dp[i][j-1] + 1
                    elif j == 0 and i != 0:
                        dp[i][j] = dp[i-1][j] + 1
                    elif i > 0 and j > 0:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
        
        # search from bottom-right
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i == m - 1 and j != n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
                    elif j == n - 1 and i != m - 1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                    elif i < m - 1 and j < n - 1:
                        dp[i][j] = min(dp[i][j], min(dp[i+1][j], dp[i][j+1]) + 1)
        
        return dp
