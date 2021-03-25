# https://leetcode.com/problems/regular-expression-matching/

# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where:

# The matching should cover the entire input string (not partial).

###############################################################################

# dp[i,j] = isMatch(first i chars in s, first j chars in p)
# get dp[i,j] by checking p[j-1]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)
        
        # initialize dp
        dp = [[False for _ in range(pLen + 1)] for _ in range(sLen + 1)]
        dp[0][0] = True
        
        # check p to match "", note "a*b*c*" can match ""
        for j in range(2, pLen + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, sLen + 1):
            for j in range(1, pLen + 1):
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    case1 = dp[i][j-2] # use "*" 0 times
                    case2 = dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == ".") # use "*" n times
                    dp[i][j] = case1 or case2
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]

        return dp[sLen][pLen]