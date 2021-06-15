# https://leetcode.com/problems/interleaving-string/

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1
# and s2.

# An interleaving of two strings s and t is a configuration where they are divided
# into non-empty substrings such that:

# Note: a + b is the concatenation of strings a and b.

################################################################################

# dp[i][j] = if can interleave A (first i chars) and B (first j chars) to get C (first i + j chars)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        # initialize
        dp[0][0] = True
        for i in range(1, n1 + 1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True
        for j in range(1, n2 + 1):
            if dp[0][j-1] and s2[j-1] == s3[j-1]:
                dp[0][j] = True
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]: # ith char in A = (i+j)th car in C
                    dp[i][j] = True
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]: # jth char in B = (i+j)th car in C
                    dp[i][j] = True
        
        return dp[-1][-1]
