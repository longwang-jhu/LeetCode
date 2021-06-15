# https://leetcode.com/problems/ones-and-zeroes/

# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's
# and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

################################################################################

# backpack -> dp[i][j][k] = strs[0...i-1] with 0's < j and 1's < k

from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.findMaxForm_2d(strs, m, n)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        
        for i in range(1, len(strs) + 1):
            s = strs[i-1]
            counts = Counter(s)
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i-1][j][k] # not use strs[i]
                    if j >= counts['0'] and k >= counts['1']:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-counts['0']][k-counts['1']] + 1)
        return dp[-1][-1][-1]
    
    def findMaxForm_2d(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, len(strs) + 1):
            s = strs[i-1]
            counts = Counter(s)
            for j in range(m, counts['0'] - 1, - 1):
                for k in range(n, counts['1'] - 1, - 1):
                    dp[j][k] = max(dp[j][k], dp[j-counts['0']][k-counts['1']] + 1)
        return dp[-1][-1]
