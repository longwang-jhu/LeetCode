# https://leetcode.com/problems/minimum-falling-path-sum-ii/

# Given a square grid of integers arr, a falling path with non-zero shifts is a
# choice of exactly one element from each row of arr, such that no two elements
# chosen in adjacent rows are in the same column.

# Return the minimum sum of a falling path with non-zero shifts.

###############################################################################

# dp[m][n] = minimum sum for reaching (m,n)
# find two minimums from the previous row

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # initialize first row
        for j in range(n):
            dp[0][j] = arr[0][j]

        # loop over each row
        for i in range(1, n):
            min_1st, min_2nd = heapq.nsmallest(2, dp[i-1])
            for j in range(n):
                if dp[i-1][j] == min_1st:
                    dp[i][j] = arr[i][j] + min_2nd
                else:
                    dp[i][j] = arr[i][j] + min_1st
        return min(dp[-1])