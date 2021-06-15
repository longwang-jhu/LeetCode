# https://leetcode.com/problems/minimum-falling-path-sum/

# Given an n x n array of integers matrix, return the minimum sum of any falling
# path through matrix.

# A falling path starts at any element in the first row and chooses the element in
# the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col -
# 1), (row + 1, col), or (row + 1, col + 1).

################################################################################

# dp[m][n] = minimum sum for reaching (m,n)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # initialize first row
        for j in range(n):
            dp[0][j] = matrix[0][j]
            
        # loop over each row
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                     dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        
        return min(dp[-1])
