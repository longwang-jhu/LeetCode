# https://leetcode.com/problems/distinct-subsequences/

# Given two strings s and t, return the number of distinct subsequences of s which
# equals t.

# A string's subsequence is a new string formed from the original string by
# deleting some (can be none) of the characters without disturbing the remaining
# characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while
# "AEC" is not).

# It is guaranteed the answer fits on a 32-bit signed integer.

################################################################################

# dp[i][j] = number of distinct subseq of s (first i chars) == t (first j chars)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n_s, n_t = len(s), len(t)
        dp = [[0 for _ in range(n_t + 1)] for _ in range(n_s + 1)]
        
        # initialize
        for i in range(n_s + 1):
            dp[i][0] = 1 # empty is a subseq that can match empty
        
        for i in range(1, n_s + 1):
            for j in range(1, n_t + 1):
                dp[i][j] = dp[i-1][j] # ignore ith char
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1] # match first j-1 chars
        
        return dp[-1][-1]
