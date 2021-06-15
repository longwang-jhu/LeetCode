# https://leetcode.com/problems/edit-distance/

# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.

# You have the following three operations permitted on a word:

###############################################################################

# dp[i][j] = number of ops to make A (frist i chars) == B (frist j chars)

# other: ans = max(len(A), len(B)) - longest common subseq

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        # initialize
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for j in range(1, n2 + 1):
            dp[0][j] = j
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1) # del the new char
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]) # no ops
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1) # replace
        
        return dp[-1][-1]