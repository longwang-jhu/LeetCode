# https://leetcode.com/problems/maximal-square/

# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.

################################################################################

# dp[i][j] = square size with bottom-right corner at (i,j)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        # base
        for i in range(m): # first col
            dp[i][0] = int(matrix[i][0])
        for j in range(n): # first row
            dp[0][j] = int(matrix[0][j])
        
        # dp
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    # check if can expand
                    if matrix[i-1][j-1] == "1":
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1     
        
        return max(map(max, dp)) ** 2
