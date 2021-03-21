# dp[row, idx] = minimum sum start from [row, idx]
# loop from bottom row, improve dp to 1D

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_row = len(triangle)
        dp = triangle[-1] # assign last row
        
        # loop backwards for each row
        for row_idx in range(n_row - 2, -1, -1):
            for i in range(row_idx + 1): # each row has row_idx + 1 elements
                dp[i] = min(dp[i], dp[i+1]) + triangle[row_idx][i]
        
        return dp[0]