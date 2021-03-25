# https://leetcode.com/problems/longest-common-subsequence/

# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.

# A common subsequence of two strings is a subsequence that is common to both
# strings.

###############################################################################

# dp[i][j] = LCS of text1 (first i chars) and text2 (first j chars)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return dp[-1][-1]